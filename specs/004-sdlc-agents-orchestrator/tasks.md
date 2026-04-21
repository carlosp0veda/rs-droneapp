---
description: "Task list for SDLC Agents and Orchestrator implementation"
---

# Tasks: SDLC Agents and Orchestrator

**Input**: Design documents from `/specs/003-sdlc-agents-orchestrator/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/cli.md

**Tests**: Test tasks are included as requested by the Project Constitution for core logic.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to (US1, US2, US3)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure for `backend/agents/` and `backend/orchestrator/` per implementation plan
- [ ] T002 [P] Install `google-adk`, `pydantic`, and `pytest-asyncio` dependencies
- [ ] T003 [P] Configure `pytest` and `black`/`isort` for the new backend modules

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure for agentic orchestration

- [ ] T002 Implement base agent and tool abstractions in `backend/agents/base.py`
- [ ] T005 [P] Implement state modeling and Pydantic schemas in `backend/orchestrator/state.py`
- [ ] T006 [P] Implement workflow wrapper definitions (Sequential, Parallel, Loop) in `backend/orchestrator/workflow.py`
- [ ] T007 Implement basic file-system tools (read/write/search) for use by agents in `backend/agents/tools.py`

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Feature Autopilot (Priority: P1) 🎯 MVP

**Goal**: Automate the flow from feature description to approved specification.

**Independent Test**: Run `python3 backend/orchestrator/cli.py init "test feature"` and verify `spec.md` is generated.

### Implementation for User Story 1

- [ ] T008 [P] [US1] Implement the Specifier Agent in `backend/agents/specifier.py`
- [ ] T009 [P] [US1] Implement the Planner Agent in `backend/agents/planner.py`
- [ ] T010 [US1] Implement the core state machine logic in `backend/orchestrator/engine.py`
- [ ] T011 [US1] Implement CLI commands `init` and `approve` in `backend/orchestrator/cli.py`
- [ ] T012 [US1] Add unit tests for `engine.py` state transitions in `backend/tests/orchestrator/test_engine_us1.py`

**Checkpoint**: User Story 1 (MVP) fully functional and testable independently

---

## Phase 4: User Story 2 - Specialized Agent Collaboration (Priority: P2)

**Goal**: Enable parallel review and iterative coding cycles.

**Independent Test**: Mock a code change and verify the Reviewer Agent identifies issues in parallel with the Coder Agent.

### Implementation for User Story 2

- [ ] T013 [P] [US2] Implement the Coder Agent in `backend/agents/coder.py`
- [ ] T014 [P] [US2] Implement the Reviewer Agent in `backend/agents/reviewer.py`
- [ ] T015 [US2] Update `orchestrator/engine.py` to support `ParallelAgent` for concurrent review tasks
- [ ] T016 [US2] Implement `LoopAgent` logic for automated fix-test cycles in `backend/orchestrator/engine.py`
- [ ] T017 [US2] Add integration tests for parallel review flow in `backend/tests/agents/test_collaboration.py`

**Checkpoint**: User Stories 1 and 2 now work independently and together

---

## Phase 5: User Story 3 - Human-in-the-Loop Governance (Priority: P3)

**Goal**: Provide tools for monitoring status and manually overriding agent decisions.

**Independent Test**: Trigger a "fix" command via CLI and verify it influences the next agent cycle.

### Implementation for User Story 3

- [ ] T018 [US3] Implement `status` and `fix` CLI commands in `backend/orchestrator/cli.py`
- [ ] T019 [US3] Implement "Manual Approval" gate state in `orchestrator/engine.py`
- [ ] T020 [US3] Implement history/trace logging to files for user inspection in `backend/orchestrator/state.py`

**Checkpoint**: All user stories are now independently functional and governess is enabled

---

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T021 [P] Ensure 100% docstring coverage per Project Constitution
- [ ] T022 Code cleanup and modularity audit (SOLID/DRY)
- [ ] T023 [P] Final performance validation of state transitions and agent response times
- [ ] T024 Validate full end-to-end flow using `quickstart.md` scenarios

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on T001, T002.
- **User Stories (Phase 3+)**: All depend on Phase 2 completion.
  - US1 (P1) is the MVP and should be completed first.
  - US2 (P2) and US3 (P3) can technically proceed in parallel once the foundation and US1 core are stable.

### Parallel Opportunities

- T002 and T003 can run together.
- T005, T006, and T007 can run together.
- Once the base agents are defined, US1 Specifier (T008) and Planner (T009) can be implemented in parallel.
- US2 Coder (T013) and Reviewer (T014) can be implemented in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Setup and Foundational phases.
2. Complete US1 (T008 - T012).
3. **VALIDATE**: Run a full spec-to-plan cycle for a simple feature.

### Incremental Delivery

1. Foundation -> Bare-bones execution.
2. US1 -> Specification & Planning automation.
3. US2 -> Collaborative Coding & Review.
4. US3 -> Human Governance and Status tracking.
