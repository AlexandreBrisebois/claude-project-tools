---
name: project
description: Sync files between the local project/ directory and a Claude Project (push, pull, init)
user-invocable: true
---

Invoke the `project` subagent to handle the requested sync operation.

Pass the full command and arguments to the agent exactly as the user typed them.

Examples:
- `/project init` → run project:init workflow
- `/project push` → push all files in project/
- `/project push file.md` → push a specific file
- `/project pull` → pull all files
- `/project pull file.md` → pull a specific file
