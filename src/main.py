from __future__ import annotations

import argparse
import csv
import logging
import sys
from pathlib import Path

import config

HERE = Path(__file__).resolve().parent
ROOT_DIR = HERE.parent
EXAMPLES_DIR = ROOT_DIR / "examples"
DEFAULT_INPUT = EXAMPLES_DIR / "sample_input.csv"
DEFAULT_OUTPUT = ROOT_DIR / "output" / "notification_plan.csv"

logging.basicConfig(
    level=logging.INFO,
    format="[SheetsSlackBot] %(levelname)s - %(message)s",
)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a Slack notification plan from a CSV export.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT,
                        help="input CSV (default: examples/sample_input.csv)")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT,
                        help="plan CSV (default: output/notification_plan.csv)")
    return parser.parse_args()


def _ensure_demo_input() -> None:
    if DEFAULT_INPUT.exists():
        return
    EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    with DEFAULT_INPUT.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["channel", "username", "message", "send"])
        writer.writerow(["#alerts", "Bot", "New lead signed up", "yes"])
        writer.writerow(["#alerts", "Bot", "Just a draft", "no"])


def _should_send(flag: str) -> bool:
    v = (flag or "").strip().lower()
    return v in {"yes", "y", "true", "1"}


def run() -> None:
    args = _parse_args()
    if args.input == DEFAULT_INPUT:
        _ensure_demo_input()
    if not args.input.exists():
        logging.error("Input file not found: %s", args.input)
        sys.exit(1)

    with args.input.open(newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    if not rows:
        logging.warning("No notifications to process.")
        return

    out_fieldnames = fieldnames + ["planned_action"]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=out_fieldnames)
        writer.writeheader()
        for row in rows:
            if _should_send(row.get("send", "")):
                action = "would_send"
            else:
                action = "skip"
            row["planned_action"] = action
            writer.writerow(row)

    if config.DEMO_MODE:
        logging.info("DEMO mode: no real Slack calls; plan saved to %s", args.output)
    else:
        logging.info("LIVE mode not implemented; only planning is supported.")


if __name__ == "__main__":
    run()
