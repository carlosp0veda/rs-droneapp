<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan:
specs/002-drone-operator-flow/plan.md
<!-- SPECKIT END -->

## Repository Guidance for Agents

### Scope

This repository contains a full-stack drone delivery application with:

- `backend/` for API, business logic, and GIS-enabled data access.
- `frontend/` for operator and dispatcher user interfaces.
- `specs/` for feature specifications and implementation planning artifacts.

### Working Agreement

1. Read the active spec artifacts before implementing behavior changes:
   - `specs/002-drone-operator-flow/spec.md`
   - `specs/002-drone-operator-flow/plan.md`
   - `specs/002-drone-operator-flow/tasks.md` (when available)
2. Prefer minimal, targeted changes that match the existing architecture.
3. Keep backend and frontend contract changes synchronized.
4. Add or update automated tests for behavior changes:
   - backend: pytest
   - frontend: vitest
5. Do not remove or modify the `SPECKIT START/END` block above.

### Quality Checks

- Run relevant tests for touched areas.
- Ensure user-facing flows for route progression remain consistent:
  Arrived -> Successful/Failed -> Departed.
- Preserve offline buffering and synchronization behavior when touching status
  update logic.
