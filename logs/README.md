# Claude activity log

`session-log.jsonl` is written by the `.claude/hooks/log_tool_use.py` hook,
registered for `PreToolUse` and `PostToolUse` in `.claude/settings.json`.

Every tool call Claude makes in this repo (Bash commands like git push/pull/
fetch, mkdir, test runs, file edits, etc.) appends one JSON line here with:

- `hook_event` — `PreToolUse` or `PostToolUse`
- `tool_name` — e.g. `Bash`, `Write`, `Edit`
- `tool_input` — the command/args Claude ran
- `tool_response` — the result (present on `PostToolUse` only)
- `logged_at`, `session_id`, `cwd`

This only captures actions taken through Claude Code's own tools in this
project, not commands run manually in a separate terminal.

Commits to this file are made manually/on request, not automatically on
every action, to avoid noisy commit history.
