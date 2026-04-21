# Tasks: Unified Docker Orchestration

**Feature**: [Unified Docker Orchestration](../spec.md)
**Status**: Ready for Implementation (Refined with Health Checks)

## Phase 1: Setup

- [x] T001 Create backend environment template in `backend/.env.example`
- [x] T002 [P] Create frontend environment template in `frontend/.env.example`

## Phase 2: Foundational

- [x] T003 [P] Update backend settings and Dockerfile to support containerized host resolution in `backend/core/settings.py` and `backend/Dockerfile`
- [x] T002 [P] Create Node.js development container with pnpm support in `frontend/Dockerfile`
- [x] T005 [P] Create PostGIS initialization script to enable spatial extensions in `db/init-spatial.sql`

## Phase 3: User Story 1 - Single Command Start [US1]

- [x] T006 [US1] Implement health check API endpoint in `backend/drone_delivery/views.py` and service routing in `backend/drone_delivery/urls.py`
- [x] T007 [US1] Initialize root `docker-compose.yml` with version 3.8+ and unified network `droneapp-network`
- [x] T008 [US1] [P] Configure PostGIS database service with healthcheck and init script in `docker-compose.yml`
- [x] T009 [US1] Configure Django backend service with healthcheck, `depends_on` (db), and volume mounts in `docker-compose.yml`
- [x] T010 [US1] Configure Vite frontend service with healthcheck, `depends_on` (backend), and volume mounts in `docker-compose.yml`
- [x] T011 [US1] Define bridge network `droneapp-network` in `docker-compose.yml`

## Phase 4: User Story 2 - Seamless Service Connectivity [US2]

- [x] T012 [US2] Update API client configuration in `frontend/src/services/api.ts` for internal network resolution (`http://backend:8000`)
- [x] T013 [US2] Verify backend-to-database connectivity via `db` service alias in `backend/core/settings.py`

## Phase 5: Polish & Verification

- [/] T014 Verify full stack build and measure startup duration (Target < 60s) via `docker compose up --build` [WAITING FOR USER]
- [/] T015 [P] Validate container health status via `docker compose ps` (all services should be `healthy`) [WAITING FOR USER]
- [/] T016 [P] Validate hot-reloading functionality (<5s) for both frontend and backend [WAITING FOR USER]
- [x] T017 Ensure `.env` files and data volumes are excluded from version control in `.gitignore`

## Dependencies

- **US1 Completion**: Requires T001-T011
- **US2 Completion**: Requires US1 + T012-T013
- **Feature Ready**: Requires all tasks completed (T001-T017)

## Parallel Execution Examples

- **Foundational Work**: T001-T005 are independent.
- **Service Config**: T008, T009, T010 can be developed in parallel once the compose structure is set.

## Implementation Strategy

1. **Core Services**: Set up Dockerfiles and base configuration.
2. **Health & Orchestration**: Implement health endpoints first, then use them for intelligent container startup in Compose.
3. **Connectivity**: Bridge the services and verify internal routing.
4. **Verification**: Final build, health, and performance validation.
