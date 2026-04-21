# Tasks: Drone Operator Delivery Flow

**Input**: Design documents from `/specs/002-drone-operator-flow/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/

**Tests**: Automated tests are MANDATORY for all business logic to align with Constitution Principle III. Tests must be written and failing before implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and GIS dependency configuration

- [ ] T001 Create project structure folders per plan in `backend/` and `frontend/`
- [ ] T002 Configure GIS dependencies (`djangorestframework-gis` in `backend/pyproject.toml` and `react-leaflet` in `frontend/package.json`)
- [ ] T003 [P] Configure PostGIS database extension in `db/init-spatial.sql`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data models and state management that block all user stories

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T002 Define `Dispatcher`, `Route`, and `Stop` models with GIS fields in `backend/drone_delivery/models.py`
- [ ] T005 [P] Create and run PostGIS migrations in `backend/`
- [ ] T006 [P] Initialize Zustand store for route state in `frontend/src/store/deliveryStore.ts`
- [ ] T007 [P] Create base API router and register `drone_delivery` app in `backend/core/urls.py`

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Route Execution (Priority: P1) 🎯 MVP

**Goal**: Enable operators to view a stop list and transition through arrival, completion (success/fail), and departure.

**Independent Test**: Assign a route via Django admin; verify stop list shows in UI; verify clicking Arrived/Complete/Depart updates stop status in DB and triggers dispatcher notifications for failures.

### Automated Tests for User Story 1 (Constitution Principle III) ⚠️

- [ ] T008 [P] [US1] Create unit tests for `Route` and `Stop` models and status transitions in `backend/tests/test_models.py`
- [ ] T009 [P] [US1] Create integration tests for stop status API endpoints and dispatcher notifications in `backend/tests/test_api.py`
- [ ] T010 [P] [US1] Create unit tests for Zustand store and offline buffering logic in `frontend/src/store/deliveryStore.test.ts`

### Implementation for User Story 1

- [ ] T011 [P] [US1] Create `StopSerializer` and `RouteSerializer` in `backend/drone_delivery/serializers.py`
- [ ] T012 [US1] Implement `GET /api/operator/route/` endpoint in `backend/drone_delivery/views.py`
- [ ] T013 [US1] Implement action-based status updates (arrive, complete, depart) with failure notifications in `backend/drone_delivery/views.py`
- [ ] T014 [P] [US1] Create `StopCard` component for stop list display in `frontend/src/features/delivery/StopCard.tsx`
- [ ] T015 [P] [US1] Create `StatusControls` for Arrive/Complete/Depart actions in `frontend/src/features/delivery/StatusControls.tsx`
- [ ] T016 [US1] Implement `OperatorDashboard` page with stop list in `frontend/src/pages/OperatorDashboard.tsx`
- [ ] T017 [US1] Integrate Zustand store with backend API calls in `frontend/src/services/api.ts`
- [ ] T018 [US1] Add offline status buffering logic via `idb-keyval` in `frontend/src/store/deliveryStore.ts`

**Checkpoint**: User Story 1 (MVP) is functional and testable independently.

---

## Phase 4: User Story 2 - Navigation Guidance (Priority: P2)

**Goal**: Provide a map view showing the route, current location, and active destination.

**Independent Test**: Load dashboard; verify map displays and correctly marks stops; verify own location updates on map.

### Automated Tests for User Story 2

- [ ] T019 [P] [US2] Create unit tests for tracking hook and geolocation data processing in `frontend/src/hooks/useTracking.test.ts`
- [ ] T020 [P] [US2] Map component rendering verification in `frontend/src/features/delivery/RouteMap.test.tsx`

### Implementation for User Story 2

- [ ] T021 [P] [US2] Initialize Leaflet map with high-contrast tiles (High Glare Support) in `frontend/src/features/delivery/RouteMap.tsx`
- [ ] T022 [US2] Add route polyline and stop markers to the map using GIS data from API in `frontend/src/features/delivery/RouteMap.tsx`
- [ ] T023 [US2] Integrate `RouteMap` into `OperatorDashboard.tsx`
- [ ] T024 [P] [US2] Implement operator location tracking using Browser Geolocation API in `frontend/src/hooks/useTracking.ts`

**Checkpoint**: User Story 2 is functional; both stories now work together.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: UX refinements, performance verification, and documentation

- [ ] T025 [P] Add high-contrast CSS overrides for glare resistance in `frontend/src/index.css`
- [ ] T026 [P] Create mock data seeding script for Dispatchers and Routes in `backend/drone_delivery/management/commands/seed_operator_route.py`
- [ ] T027 [US1] Verify SC-002: Test sync latency < 2s under simulated connectivity transitions
- [ ] T028 [US1] Verify SC-003: Audit log completeness for a full route execution
- [ ] T029 [P] Final verification of `quickstart.md` steps and `AGENTS.md` context
- [ ] T030 Run end-to-end traversal of a full route in dev environment

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can start immediately.
- **Foundational (Phase 2)**: Depends on Setup (GIS config). BLOCKS user stories.
- **User Stories (Phase 3+)**: Depend on Foundational completion. US1 (P1) is the focus for MVP.
- **Polish (Phase 5)**: Depends on US1/US2 completion.

### User Story Dependencies

- **User Story 1 (P1)**: Independent of US2.
- **User Story 2 (P2)**: Integrates with US1 components (Dashboard) but can be built in parallel if mock data is used.

### Parallel Opportunities

- All tasks marked `[P]` can run in parallel within their respective phases.
- Test creation (T008-T010) happens in parallel before implementation.
- Backend API development (T011-T013) can run in parallel with Frontend UI development once contracts are stable.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete GIS Setup and Foundational Models (including `Dispatcher`).
2. Build the Backend API for Route retrieval and Stop status updates with failure notifications.
3. Build the stop list UI (Dashboard + StopCard).
4. **Checkpoint**: Validate that an operator can execute a route list without a map and failures notify the dispatcher.

### Full Feature
1. Add Map navigation (US2).
2. Add Offline support (T018).
3. Verify SC-002 and SC-003 metrics.
4. Final polish and documentation.
