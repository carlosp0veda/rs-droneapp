# Feature Specification: Unified Docker Orchestration

**Feature Branch**: `003-unified-docker-compose`  
**Created**: 2026-04-20  
**Status**: Draft  
**Input**: User description: "create a unified docker-compose to enable running the whole app with one command, backend and frontend should have their own Dockerfile with a root docker-compose.yml that bridges both through a unified network"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Single Command Start (Priority: P1)

As a developer, I want to start the entire application ecosystem with a single command so that I can begin development immediately without manual service management.

**Why this priority**: Core requirement for developer productivity and environment consistency.

**Independent Test**: Can be fully tested by running `docker compose up` and verifying all services (web, api, db) start successfully.

**Acceptance Scenarios**:

1. **Given** a clean repository, **When** running `docker compose up`, **Then** the database, backend, and frontend containers are built and started synchronously.
2. **Given** services are running, **When** checking container status, **Then** all three services show a healthy/running state.

---

### User Story 2 - Seamless Service Connectivity (Priority: P1)

As a developer, I want the frontend and backend to communicate over a private network using service aliases so that I don't have to manage IP addresses or host-specific configurations.

**Why this priority**: Required for the application to function as a unified system within the containerized environment.

**Independent Test**: Verify that frontend requests to the API service alias (e.g., `http://backend:8000`) resolve correctly within the Docker network.

**Acceptance Scenarios**:

1. **Given** the stack is running, **When** the frontend attempts to fetch data from the API, **Then** the request is successfully routed to the backend container over the unified network.
2. **Given** a database dependency, **When** the backend starts, **Then** it successfully connects to the database service using the service name alias.

---

### Edge Cases

- **PostGIS Extension Initialization**: How does the system handle the first-time setup of spatial extensions in the database container?
- **Build Failures**: How does the system handle cases where `frontend/Dockerfile` fails due to missing dependencies in the host's `pnpm-lock.yaml`?
- **Port Conflicts**: What happens if ports 8000 (backend) or 5173 (frontend) are already occupied on the host machine?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: A root `docker-compose.yml` MUST be created to orchestrate all application services.
- **FR-002**: A `frontend/Dockerfile` MUST be created to containerize the React/Vite application.
- **FR-003**: The `backend` service MUST utilize the existing `backend/Dockerfile`, ensuring all GeoDjango/PostGIS dependencies are correctly handled.
- **FR-002**: A dedicated Docker network MUST be defined to bridge all services, allowing internal communication via service names.
- **FR-005**: A PostgreSQL/PostGIS service MUST be included in the compose file to satisfy backend data requirements.
- **FR-006**: Environment variables MUST be used to configure sensitive or environment-specific values (DB credentials, API URLs).
- **FR-007**: Volume mounting MUST be configured to allow live-reloading during development for both frontend and backend.

### Key Entities *(include if feature involves data)*

- **Docker Compose Stack**: Represents the collection of services (frontend, backend, db) running as a unit.
- **Service Bridge Network**: The virtual network facilitating inter-service communication.
- **Persistent Volume**: Storage entities for database data and potential media uploads.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Total time to start the entire stack from `docker compose up` (assuming cached base images) is under 60 seconds.
- **SC-002**: 100% of services (backend, frontend, database) report a 'running' status in `docker compose ps`.
- **SC-003**: Frontend application is accessible at `http://localhost:5173` with a valid response.
- **SC-002**: Backend API is accessible at `http://localhost:8000/admin/` (or equivalent endpoint) with a valid response.
- **SC-005**: Changes to local components or backend views are reflected within 5 seconds inside the running containers (hot-reloading verification).

## Assumptions

- The backend expects a PostGIS-compatible database.
- The frontend uses `pnpm` as its primary package manager.
- Developers have Docker and Docker Compose (v2 or higher) installed on their host machines.
- The backend's `requirements.txt` and frontend's `package.json` are up-to-date and valid.
