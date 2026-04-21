# Quickstart: Drone Delivery Run

## Local Development Setup

### 1. Prerequisites
- Docker & Docker Compose
- Mapbox Access Token (Sign up at [mapbox.com](https://www.mapbox.com/))
- Python 3.12+
- Node.js 20+

### 2. Environment Configuration
Create `.env` files in both `backend/` and `frontend/` directories.

**Backend (`backend/.env`)**:
```env
DEBUG=True
SECRET_KEY=your-django-secret
DATABASE_URL=postgres://drone_user:drone_pass@localhost:5432/drone_db
REDIS_URL=redis://localhost:6379/1
```

**Frontend (`frontend/.env`)**:
```env
VITE_MAPBOX_TOKEN=your_mapbox_token
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

### 3. Backend Execution
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 4. Frontend Execution
```bash
cd frontend
pnpm install
pnpm run dev
```

## Running Tests

### Backend (pytest)
```bash
cd backend
pytest
```

### Frontend (Vitest)
```bash
cd frontend
pnpm test
```

## Verification Steps
1. Navigate to `http://localhost:5173`.
2. Verify the map loads (requires valid Mapbox token).
3. Ensure the Sidebar displays mock delivery data if backend is not yet populated.
