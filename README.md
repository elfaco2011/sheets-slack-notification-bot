# Google Sheets to Slack Automation Bot

## 🔍 Problem
Manually monitoring Google Sheets and deciding when to send Slack notifications is repetitive and error-prone, especially for teams working with structured data.

## ✅ Solution
This Python automation bot reads spreadsheet rows, evaluates custom conditions, and prepares Slack messages automatically, turning spreadsheet data into actionable notifications.


Notification planner that turns spreadsheet rows into Slack messages. In DEMO mode it does **not** call Slack; it only prepares a sending plan.

## 🚀 Features
- Reads `examples/sample_input.csv` with columns `channel, username, message, send`.
- Decides whether each row should be sent (`would_send`) or `skip`.
- Writes the plan to `examples/sample_output.csv`.

## 🛠 Tech Stack
- Python
- CSV processing
- Slack message formatting
- Workflow automation


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


## 📦 Ready-made Automation Pack
If you're looking for a plug-and-play solution, check out my automation pack on Gumroad:
👉 https://khalidelfakir.gumroad.com
