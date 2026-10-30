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
- Marks each row `would_send` when `send` is `yes`, `y`, `true` or `1` (case-insensitive), otherwise `skip`.
- Writes the plan, with the extra `planned_action` column, to `examples/sample_output.csv`.

It does not connect to Google Sheets and does not send anything to Slack: it only produces the sending plan.
`src/config.py` holds the `DEMO_MODE` flag and placeholders for a future Slack webhook integration, which is not implemented.

## Quick start
Tested with Python 3.11. No external dependencies (standard library only).

```bash
python src/main.py
```

## Sample data
`examples/sample_input.csv` contains two messages, one to send and one draft.
If the file is missing, the script recreates it before running.

## Adapting it to your data
Export your sheet as CSV with the same four column headers and save it as `examples/sample_input.csv`.
Other columns are kept and copied to the output.
