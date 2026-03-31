# Claude Code Agent Integration

This project provides scripts and configuration for integrating with Claude as a code agent.

## Key Components

- `scripts/project_init.py`: Initializes the Claude agent configuration and ensures the `project/` directory exists.
- `scripts/project_sync.py`: Handles push/pull operations between your local `project/` directory and Claude Project.
- `.claude/config.json`: Stores your Claude session key (created by `project_init.py`).
- `project/`: Directory for files to sync with Claude Project.

## Setup

1. Run `python scripts/project_init.py` to configure your session key and create the `project/` directory.
2. Use `python scripts/project_sync.py push` or `pull` to sync files.

## Security

- Never commit `.claude/config.json` (contains secrets).
- Only files in `project/` are synced.

## Troubleshooting

- If you see errors about missing config, rerun `project_init.py`.
- For push/pull errors, check your session key and network connectivity.

See `README.md` for more details.