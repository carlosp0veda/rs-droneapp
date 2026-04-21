# DroneApp

DroneApp is a full-stack web application for managing drone delivery routes.
It provides a map-based operator workflow for stop-by-stop execution and a
dispatcher view for operational monitoring and failure alerting.

## Tech Stack

- Backend: Python, Django, Django REST Framework, PostGIS
- Frontend: React, TypeScript, Vite, Leaflet
- Data: PostgreSQL + PostGIS
- Testing: pytest (backend), vitest (frontend)
- Local environment: Docker Compose

## Project Structure

```text
backend/   Django API and delivery domain logic
frontend/  React operator and dispatcher interfaces
specs/     Feature specs, plans, and implementation artifacts
```

## Current Feature Context

Active implementation details live in:

- `specs/002-drone-operator-flow/spec.md`
- `specs/002-drone-operator-flow/plan.md`
- `specs/002-drone-operator-flow/tasks.md` (if present)

## Getting Started

1. Install dependencies for each app:
   - `backend/` Python dependencies
   - `frontend/` Node dependencies
2. Start services using the project's Docker Compose flow.
3. Run tests:
   - Backend: `pytest`
   - Frontend: `npm run test`

If your local workflow differs, prefer the commands documented in the active
spec artifacts under `specs/`.
