# Implementation Plan: Unified Docker Orchestration

This plan establishes a unified, containerized development environment for the DroneApp ecosystem. It provides a single-command setup while maintaining strict environment variable security by using independent `.env` files and preventing leakage through orchestrator files.

## User Review Required

> [!IMPORTANT]
> **Environment Persistence**: The database will use a named volume (`drone_db_data`) to persist your data even if the containers are removed. If you need a completely fresh start, you will need to run `docker compose down -v`.

> [!NOTE]
> **Local Port Mapping**:
> - Frontend: http://localhost:5173
> - Backend: http://localhost:8000
> - Database: http://localhost:5432 (Internal access via `db:5432`)

## Proposed Changes

### Configuration & Security

#### [NEW] [backend/.env.example](file:///Users/cpoveda/droneapp/backend/.env.example)
Template for backend secrets and configuration.

#### [NEW] [frontend/.env.example](file:///Users/cpoveda/droneapp/frontend/.env.example)
Template for frontend environment variables (Vite-prefixed).

#### [NEW] [docker-compose.yml](file:///Users/cpoveda/droneapp/docker-compose.yml)
The root orchestrator file defining services, networks, and volumes.

---

### Frontend Infrastructure

#### [NEW] [frontend/Dockerfile](file:///Users/cpoveda/droneapp/frontend/Dockerfile)
Node.js based container setup using `pnpm` to serve the React application.

#### [MODIFY] [frontend/src/services/api.ts](file:///Users/cpoveda/droneapp/frontend/src/services/api.ts)
Ensure the API base URL is correctly resolved from the container's environment.

---

### Backend Infrastructure

#### [MODIFY] [backend/Dockerfile](file:///Users/cpoveda/droneapp/backend/Dockerfile)
Ensure the backend image is optimized for the compose network.

---

## Constitution Check

- **Principle I (Agentic-First)**: Standardized container structure makes the environment predictable for autonomous agents.
- **Principle III (Automated Testing)**: Docker Compose enables running integration tests in a clean, reproducible environment.
- **Principle V (Performance)**: Using alpine-based images and optimized layers for faster build/startup times.

## Verification Plan

### Automated Tests
1. **Service Connectivity**: Run `docker compose exec frontend ping backend` to verify network bridge.
2. **Environment Validation**: Run `docker compose exec backend env | grep DB_` to ensure variables are injected via `env_file`.
3. **Build Integrity**: Run `docker compose build --no-cache` to ensure clean builds.

### Manual Verification
1. Run `docker compose up`.
2. Verify frontend loads at `localhost:5173`.
3. Verify backend admin is accessible at `localhost:8000/admin/`.
4. Check that no `.env` files are tracked by Git (check `.gitignore`).
