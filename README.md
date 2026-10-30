# Sheets to Slack Notification Planner

## Problem
Deciding which rows of a spreadsheet should become Slack notifications is a manual, repetitive check.

## Example output
Input (`examples/sample_input.csv`, a CSV export of the sheet):

```text
channel,username,message,send
#alerts,Bot,New lead signed up,yes
#alerts,Bot,Just a draft,no
```

Output (`examples/sample_output.csv`), produced by running the script on the file above:

```text
channel,username,message,send,planned_action
#alerts,Bot,New lead signed up,yes,would_send
#alerts,Bot,Just a draft,no,skip
```

## What it does
- Reads a CSV exported from a spreadsheet with the columns `channel`, `username`, `message`, `send`.
- Marks each row `would_send` when `send` is `yes`, `y`, `true` or `1` (case-insensitive, surrounding spaces ignored), otherwise `skip`.
- Writes the plan, with the extra `planned_action` column, to `output/notification_plan.csv`.

Only the `send` column drives the decision; `channel`, `username`, `message` and any other columns are copied to the plan unchanged.

It does not connect to Google Sheets and does not send anything to Slack: it only produces the sending plan.
`src/config.py` only holds a `DEMO_MODE` flag; setting it to `False` just logs that live sending is not implemented.

## Quick start
Tested with Python 3.11. No external dependencies (standard library only).

```bash
pip install -r requirements.txt   # nothing to install
python src/main.py
```

The plan is written to `output/notification_plan.csv` (git-ignored). To use other files:

```bash
python src/main.py --input path/to/export.csv --output path/to/plan.csv
```

## Sample data
`examples/sample_input.csv` contains two messages, one to send and one draft.
If the file is missing and no `--input` is given, the script recreates it before running.

## Adapting it to your data
Export your sheet as CSV (File > Download > CSV) with a `send` column, and pass it with `--input`.
Other columns are kept and copied to the output; a file without a `send` column marks every row `skip`.
