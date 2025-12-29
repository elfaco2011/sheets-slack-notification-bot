# Sheets → Slack Notification Bot

Notification planner that turns spreadsheet rows into Slack messages. In DEMO mode it does **not** call Slack; it only prepares a sending plan.

## What it does
- Reads `examples/sample_input.csv` with columns `channel, username, message, send`.
- Decides whether each row should be sent (`would_send`) or `skip`.
- Writes the plan to `examples/sample_output.csv`.

## How to run (DEMO)
```bash
cd sheets-slack-notification-bot
python src/main.py
```

A demo `sample_input.csv` is auto-created if missing.

## Inputs & outputs
- **Input:** `examples/sample_input.csv` (messages to evaluate).
- **Output:** `examples/sample_output.csv` with `planned_action` column.

## Notes
This project is wired for future Slack API integration via `src/config.py`, but by default it runs fully offline in DEMO mode.
