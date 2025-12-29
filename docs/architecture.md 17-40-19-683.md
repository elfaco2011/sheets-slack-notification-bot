# Sheets → Slack Notification Bot – Architecture

## Overview

This bot simulates sending Slack notifications based on rows exported from a
spreadsheet. In DEMO mode it does not call the Slack API, but instead builds a
CSV plan describing which messages would be sent.

- Input: `examples/sample_input.csv`
- Output: `examples/sample_output.csv`

## Components

- `src/main.py`
  - Logging setup
  - Path resolution (relative to the bot root)
  - `read_events()` – parses the input CSV
  - `build_plan()` – decides what to do with each row
  - `write_plan()` – writes the notification plan to CSV

- `src/config.py`
  - `DEMO_MODE` flag
  - `SLACK_WEBHOOK_URL_ENV` and `DEFAULT_CHANNEL` placeholders for LIVE mode

## Data Flow

```text
User Input CSV (examples/sample_input.csv)
      │
      ▼
read_events()
      │
      ▼
build_plan()
      │
      ├── DEMO → write_plan()  (no real network calls)
      │
      └── API  → send to Slack → write_plan()  (future LIVE mode)
```

## Error Handling

- Missing input file → error log and abort.
- Invalid header → error log and abort.
- Empty `message` field → row skipped.

## Future Improvements

- Implement real Slack webhook calls when `DEMO_MODE` is False.
- Support message templates and variables.
- Filter which channels/users receive notifications.
