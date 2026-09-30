# learn-python-with-claude

Learning project for core Python concepts, built up with Claude Code.

## Structure

- `src/learn_python_with_claude/` — package source
  - `core_python_01/` — Lesson 1 and roadmap of all topics
- `tests/` — pytest tests
- `pyproject.toml` — project metadata and dependencies
- `.claude/settings.json` — Claude Code hook configuration (logging)
- `logs/session-log.jsonl` — Activity log of all Claude tool calls

## Conventions

- Python >= 3.10
- Use `pytest` for tests
- Keep lessons/exercises organized as they're added (one topic per module)
- Lesson naming: `lesson_NN_topic_name.py` (e.g., `lesson_01_running_python.py`)
- Each lesson includes: explanations, code examples, and a corresponding test file

## Logging

A Claude hook (`.claude/settings.json`) logs all tool calls to `logs/session-log.jsonl` in JSONL format:
- Each line is a valid JSON object with: `logged_at`, `hook_event`, `tool_name`, `tool_input`, `tool_response`, etc.
- Append-only format — easy to track activity over time
- Committed to `feature/claude-logs` (kept separate from code branches)

## Running Tests

```bash
python -m pytest tests/
pytest tests/test_lesson_01_running_python.py -v
```

## Merge Guard

`feature/claude-logs` holds Claude activity logs for internal learning only: other branches may merge into it, but it must never be merged into any other branch.

Enforced by:
- GitHub Actions workflow (`.github/workflows/block-logs-merge.yml`) — blocks merges on GitHub
- Local git hook (`.githooks/pre-merge-commit`) — blocks merges locally

Enable the local hook with: `git config core.hooksPath .githooks`

## Lesson Roadmap

79 topics across 11 levels (from basic syntax to advanced constructs):
- Level 1: Running Python, variables, keywords
- Level 2: Data types and operators
- Level 3-5: Strings, control flow, collections, functions
- Level 6-11: Comprehensions, exceptions, modules, OOP, decorators, async

See `src/learn_python_with_claude/core_python_01/README.md` for the full list.
