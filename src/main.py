from __future__ import annotations

import csv
import logging
from pathlib import Path

import config

HERE = Path(__file__).resolve().parent
EXAMPLES_DIR = HERE.parent / "examples"
INPUT_PATH = EXAMPLES_DIR / "sample_input.csv"
OUTPUT_PATH = EXAMPLES_DIR / "sample_output.csv"

logging.basicConfig(
    level=logging.INFO,
    format="[SheetsSlackBot] %(levelname)s - %(message)s",
)


def _ensure_demo_input() -> None:
    if INPUT_PATH.exists():
        return
    EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    with INPUT_PATH.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["channel", "username", "message", "send"])
        writer.writerow(["#alerts", "Bot", "New lead signed up", "yes"])
        writer.writerow(["#alerts", "Bot", "Just a draft", "no"])


def _should_send(flag: str) -> bool:
    v = (flag or "").strip().lower()
    return v in {"yes", "y", "true", "1"}


def run() -> None:
    _ensure_demo_input()

    with INPUT_PATH.open(newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    if not rows:
        logging.warning("No notifications to process.")
        return

    out_fieldnames = fieldnames + ["planned_action"]
    with OUTPUT_PATH.open("w", newline="") as f:
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
        logging.info("DEMO mode: no real Slack calls; plan saved to %s", OUTPUT_PATH)
    else:
        logging.info("LIVE mode not implemented; only planning is supported.")


if __name__ == "__main__":
    run()
