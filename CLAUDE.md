# learn-python-with-claude

Learning project for core Python concepts, built up with Claude Code.

## Structure

- `src/learn_python_with_claude/` — package source
- `tests/` — pytest tests
- `pyproject.toml` — project metadata and dependencies

## Conventions

- Python >= 3.10
- Use `pytest` for tests
- Keep lessons/exercises organized as they're added (one topic per module/branch)
- `feature/claude-logs` holds Claude activity logs for internal learning only: other branches may merge into it, but it must never be merged into any other branch (enforced by `.github/workflows/block-logs-merge.yml` and `.githooks/pre-merge-commit`; enable the hook with `git config core.hooksPath .githooks`)
