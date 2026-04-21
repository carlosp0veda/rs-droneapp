# Quickstart: Drone Operator Flow

## Overview
This feature implements the core delivery execution flow for drone operators, including route visualization, stop management, and status reporting.

## Prerequisites
- Docker and Docker Compose installed.
- PostgreSQL with PostGIS extension (provided by `docker-compose`).

## Setup

1. **Build and Start Services**:
   ```bash
   docker compose up --build
   ```

2. **Initialize Database**:
   ```bash
   docker compose exec backend python manage.py migrate
   ```

3. **Seed Mock Data (Optional)**:
   ```bash
   docker compose exec backend python manage.py seed_operator_route
   ```

## Development

### Backend
- Runs at `http://localhost:8000`.
- GIS support is provided via `djangorestframework-gis`.

### Frontend
- Runs at `http://localhost:5173`.
- Key components:
  - `OperatorDashboard`: Main container.
  - `RouteMap`: Leaflet-based navigation view.
  - `StopCard`: Interactive component for status updates.

### Testing
- **Backend**: `pytest`
- **Frontend**: `npm run test` (Vitest)
