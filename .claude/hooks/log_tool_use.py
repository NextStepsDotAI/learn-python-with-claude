#!/usr/bin/env python3
"""Claude Code hook: appends every tool call (and its result) to logs/session-log.jsonl.

Registered for both PreToolUse and PostToolUse in .claude/settings.json.
Reads the hook event JSON from stdin (per Claude Code hook spec) and appends
one JSON line per event to logs/session-log.jsonl at the repo root.
"""
import json
import sys
import datetime
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parents[2] / "logs" / "session-log.jsonl"


def main() -> int:
    try:
        raw = sys.stdin.read()
        event = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        event = {"raw": raw}

    entry = {
        "logged_at": datetime.datetime.utcnow().isoformat() + "Z",
        "hook_event": event.get("hook_event_name"),
        "tool_name": event.get("tool_name"),
        "tool_input": event.get("tool_input"),
        "tool_response": event.get("tool_response"),
        "session_id": event.get("session_id"),
        "cwd": event.get("cwd"),
    }

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, default=str) + "\n")

    # Always allow the tool call to proceed / continue normally.
    return 0


if __name__ == "__main__":
    sys.exit(main())
