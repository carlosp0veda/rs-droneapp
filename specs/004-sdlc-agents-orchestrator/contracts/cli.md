# CLI Contract: SDLC Orchestrator

The SDLC Orchestrator is controlled via a command-line interface.

## Commands

### `sdlc.py init`
Starts a new feature lifecycle.

**Arguments**:
- `description`: (Required) String describing the feature.
- `--short-name`: (Optional) Custom short name for the feature.
- `--workflow`: (Optional, default: `full-sdlc`) Name of the workflow to use.

**Behavior**:
1. Creates a new feature branch.
2. Initializes the `specs/[###-feature-name]/` directory.
3. Invokes the **Specifier Agent**.
4. Transitions state to `SPECIFYING`.

---

### `sdlc.py approve`
Approves the artifact generated in the current phase (Spec or Plan).

**Arguments**:
- `feature_dir`: (Optional) path to the feature directory. Defaults to current branch directory.

**Behavior**:
1. Marks the current artifact as "Approved".
2. Transitions the orchestrator to the next phase (e.g., `SPECIFYING` -> `PLANNING`).

---

### `sdlc.py status`
Shows the current status of the SDLC lifecycle for the active branch.

**Output**:
- Current Phase (e.g., `PLANNING`)
- Last Agent Action (e.g., `Planner generated plan.md`)
- Pending Approvals
- Active Agents (e.g., `Coder [RUNNING]`, `Reviewer [IDLE]`)

---

### `sdlc.py fix`
Manually triggers a fix/iteration cycle if an agent gets stuck or a user wants to force a revision.

**Arguments**:
- `instructions`: (Required) String describing what needs to be fixed.

**Behavior**:
1. Injects instructions into the current agent session.
2. Re-runs the current step.
