# Environment & Infrastructure Model

## Service Map

| Service | Image | Responsibility | Internal Alias | Port Mapping |
|---------|-------|----------------|----------------|--------------|
| `db` | `postgis/postgis:16-3.4` | Persistent spatial data storage | `db` | `5432:5432` |
| `backend` | `python:3.12-slim` | Django Rest Framework API | `backend` | `8000:8000` |
| `frontend` | `node:20-alpine` | React/Vite web application | `frontend` | `5173:5173` |

## Environment Variable Schema

### Backend (.env)
- `DEBUG`: Boolean (True/False)
- `SECRET_KEY`: Django secret key
- `DB_NAME`: Database name
- `DB_USER`: Database user
- `DB_PASSWORD`: Database password
- `DB_HOST`: Hostname (set to `db` for internal network)
- `DB_PORT`: Port (set to `5432`)
- `ALLOWED_HOSTS`: Comma-separated list

### Frontend (.env)
- `VITE_API_BASE_URL`: The URL for the backend API (accessible from the host/browser)

## Shared Network
- **Name**: `droneapp-network`
- **Driver**: `bridge`
