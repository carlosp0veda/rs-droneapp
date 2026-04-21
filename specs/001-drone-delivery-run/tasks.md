# Tasks: Drone Delivery Run

**Input**: Design documents from `/specs/001-drone-delivery-run/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story. This list follows a TDD approach as mandated by Constitution Principle III.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Initialize Django project and `drone_delivery` app in `backend/`
- [ ] T002 Initialize React (Vite) project with TypeScript in `frontend/`
- [ ] T003 Configure Webpack/Vite for PostCSS and CSS Variables in `frontend/vite.config.ts`
- [ ] T002 [P] Configure linting (Ruff/ESLint) and formatting (Black/Prettier)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 [P] Install and configure PostGIS extension in `backend/settings.py`
- [ ] T006 Create database models (Operator, DeliveryRun, Location, Order) in `backend/drone_delivery/models/`
- [ ] T007 [P] Create and apply initial spatial migrations
- [ ] T008 [P] Configure DRF and Spectacular for API documentation in `backend/drone_delivery/api/`
- [ ] T010 [P] Setup base API Client and Map services in `frontend/src/services/`

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Delivery Run Overview (Priority: P1) 🎯 MVP

**Goal**: Operator can see a full overview of the run with all locations on a map and a sequenced list.

**Independent Test**: Load a run with 2 pickups and 3 deliveries; verify 5 markers appear on map and 5 items in sidebar.

### 🧪 Tests for User Story 1

- [ ] T011 [P] [US1] Unit tests for `DeliveryRun` and `Location` models in `backend/drone_delivery/tests/test_models.py`
- [ ] T012 [P] [US1] Contract test for `GET /delivery-runs/` in `backend/drone_delivery/tests/test_contracts.py`
- [ ] T013 [P] [US1] Unit tests for `MapView` marker logic in `frontend/src/components/MapView.test.ts`

### 🏗️ Implementation for User Story 1

- [ ] T014 [US1] Implement `GET /delivery-runs/` endpoints in `backend/drone_delivery/views/`
- [ ] T015 [US1] Integration tests for Run Overview flow in `backend/drone_delivery/tests/test_views.py`
- [ ] T016 [P] [US1] Create `MapView` component using Mapbox in `frontend/src/components/MapView/`
- [ ] T017 [P] [US1] Create `LocationSidebar` component in `frontend/src/components/Sidebar/`
- [ ] T018 [US1] Implement `RunOverview` page in `frontend/src/pages/RunOverview/`

**Checkpoint**: User Story 1 fully functional and testable independently

---

## Phase 4: User Story 2 - Pickup Execution (Priority: P2)

**Goal**: Operator can identify and execute restuarant pickups.

**Independent Test**: Filter sidebar for "Pickup"; change status to "Arrived" and verify UI highlight.

### 🧪 Tests for User Story 2

- [ ] T019 [P] [US2] Unit tests for Pickup status transitions in `backend/drone_delivery/tests/test_models.py`
- [ ] T020 [P] [US2] Contract test for `PATCH /locations/{id}/` in `backend/drone_delivery/tests/test_contracts.py`

### 🏗️ Implementation for User Story 2

- [ ] T021 [US2] Implement status update views in `backend/drone_delivery/views/`
- [ ] T022 [US2] Integration tests for Pickup workflow in `backend/drone_delivery/tests/test_views.py`
- [ ] T023 [US2] Add status toggle UI (Pending -> Arrived -> Complete) to `LocationSidebar`
- [ ] T024 [P] [US2] Unit tests for status UI state logic in `frontend/src/components/Sidebar.test.ts`

---

## Phase 5: User Story 3 - Residential Delivery (Priority: P2)

**Goal**: Operator can identify residential delivery locations and follow drop-off instructions.

**Independent Test**: Navigate to a "Delivery" location; verify specific instructions (e.g. "Backyard") are displayed.

### 🧪 Tests for User Story 3

- [ ] T025 [P] [US3] Unit tests for Residential Order instructions logic in `backend/drone_delivery/tests/test_models.py`
- [ ] T026 [US3] Integration tests for Residential Delivery flow in `backend/drone_delivery/tests/test_views.py`

### 🏗️ Implementation for User Story 3

- [ ] T027 [P] [US3] Add drop-off instructions field to `LocationSidebar` UI in `frontend/src/components/Sidebar/`
- [ ] T028 [US3] Implement distinct "Delivery" marker styling and "Delivered" dimming in `MapView`

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T029 [P] Accessibility audit and WCAG 2.1 Level AA fixes in `frontend/src/styles/`
- [ ] T030 [P] Performance profiling (TTI < 2s verification) and scale testing (SC-002)
- [ ] T031 [P] Ensure 100% test coverage for core business logic per Principle III
- [ ] T032 Final verify against all scenarios in `quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Phase 1; blocks all User Stories.
- **User Stories (Phase 3+)**: All depend on Phase 2.
- **TDD Requirement**: Task IDs for tests (T011, T012, T013, etc.) MUST be implemented first for each story.

---

## Implementation Strategy

### TDD Workflow (Per User Story)

1. Implement Unit/Contract tests.
2. Run tests to verify failure.
3. Implement core logic (models/views).
4. Run tests to verify success.
5. Create UI components and integrate.

### MVP Scope (User Story 1 Only)

1. Complete Phase 1 & 2.
2. Complete US1 tests and UI.
3. Verify basic run overview.
