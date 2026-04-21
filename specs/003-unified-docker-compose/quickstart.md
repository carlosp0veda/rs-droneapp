# Quickstart: Unified Docker Environment

Welcome to the unified development environment for DroneApp. This setup allows you to run the entire stack (Database, Backend, and Frontend) with a single command.

## Prerequisites
- Docker Desktop or Docker Engine installed.
- `pnpm` installed locally (optional, for local development outside Docker).

## Initial Setup

1. **Configure Environment Variables**:
   Copy the example files and update them with your local configurations (keys are already pre-configured for local dev):
   ```bash
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env
   ```

2. **Start the Stack**:
   ```bash
   docker compose up --build
   ```

## Key Endpoints
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **Database**: localhost:5432 (User: `postgres`, Pass: `postgres`)

## Development Workflow
- **Hot Reloading**: Both frontend and backend are configured with volume mounts. Saving changes locally will trigger automatic reloads inside the containers.
- **Migrations**: To run database migrations, use:
  ```bash
  docker compose exec backend python manage.py migrate
  ```
- **Stopping**:
  ```bash
  docker compose down
  ```
  *(Add `-v` to also remove internal database data)*
