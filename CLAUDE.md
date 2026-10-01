# learn-python-with-claude

Learning project for core Python concepts, built up with Claude Code.

## Structure

- `src/learn_python_with_claude/` — package source
- `tests/` — pytest tests
- `pyproject.toml` — project metadata and dependencies

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

## Workflow Enforcement

All changes to `main` must go through pull requests. Enforced with defense-in-depth:

### Local Git Hooks (`.githooks/`)
Enable with: `git config core.hooksPath .githooks`

- **`pre-commit`** — Blocks `git commit` directly to main
- **`pre-push`** — Blocks `git push` directly to main
- **`pre-merge-commit`** — Blocks merging `feature/claude-logs` into other branches

All can be bypassed with `--no-verify` if absolutely necessary (not recommended).

### GitHub Actions Workflows (`.github/workflows/`)

- **`enforce-pr-workflow.yml`** — Detects direct commits that reach main and fails the build
  - Allows: PR merges, initial commit
  - Rejects: direct commits outside of PRs
  
- **`block-logs-merge.yml`** — Prevents `feature/claude-logs` from being merged into other branches
  - Allows: other branches merging into `feature/claude-logs`
  - Rejects: `feature/claude-logs` merging out

### Workflow Process

1. **Create feature branch** from main
2. **Commit locally** (blocked from main by `pre-commit` hook)
3. **Push branch** (blocked from main by `pre-push` hook)
4. **Open PR** on GitHub
5. **Merge PR** (workflows validate and allow merge)
6. **Other branches receive updates** via `git merge origin/main`

## Lesson Roadmap

79 topics across 11 levels (from basic syntax to advanced constructs):
- Level 1: Running Python, variables, keywords
- Level 2: Data types and operators
- Level 3-5: Strings, control flow, collections, functions
- Level 6-11: Comprehensions, exceptions, modules, OOP, decorators, async

See `src/learn_python_with_claude/core_python_01/README.md` for the full list.
