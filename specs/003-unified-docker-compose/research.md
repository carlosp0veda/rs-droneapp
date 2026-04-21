# Research: Unified Docker Orchestration & Environment Security

## Decision 1: Environment Variable Management
**Decision**: Use `env_file` in `docker-compose.yml` combined with `.env.example` templates.
**Rationale**: 
- `env_file` prevents sensitive values from appearing in `docker-compose.yml` or being baked into `Dockerfile` instructions (which can be inspected via `docker history`).
- Independent `.env` files for frontend and backend allow for clean separation of concerns.
- `.env.example` provides a blueprint without exposing actual secrets.

**Alternatives Considered**:
- Using `environment:` key in `docker-compose.yml`: Rejected because it leaks values to anyone with access to the source code.
- Baking `.env` into `Dockerfile`: Rejected due to security (secrets in image layers) and lack of flexibility.

## Decision 2: Network Topology
**Decision**: Use a single bridge network named `droneapp-network`.
**Rationale**: 
- Services can communicate using their container names as hostnames (e.g., `http://backend:8000`).
- Provides isolation from the host network while maintaining internal connectivity.

## Decision 3: Frontend Container Strategy
**Decision**: Use a Node-based container running the Vite dev server with volume mounts.
**Rationale**: 
- Supports Hot Module Replacement (HMR) during development.
- Aligning with the backend's `manage.py runserver` approach for a consistent "development-first" container experience.

## Decision 4: Database Strategy
**Decision**: Use `postgis/postgis:16-3.4` with a named volume.
**Rationale**: 
- Required for GeoDjango (`django.contrib.gis`).
- Named volume ensures data persistence across container restarts and recreation.

## Open Questions Resolved
- **Q**: How to handle Vite's need for `VITE_` prefix?
- **A**: The `.env` file for the frontend will explicitly use the `VITE_` prefix, which Vite's dev server picks up automatically.
