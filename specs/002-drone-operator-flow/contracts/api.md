# API Contracts: Drone Operator Flow

## 1. Active Route Retrieval
Endpoint to fetch the current assigned route for the logged-in operator.

- **URL**: `/api/operator/route/`
- **Method**: `GET`
- **Success Response**: `200 OK`
- **Payload**:
```json
{
  "id": "uuid",
  "status": "IN_PROGRESS",
  "drone": "DRONE-001",
  "stops": [
    {
      "id": "uuid",
      "sequence": 1,
      "type": "PICKUP",
      "status": "PENDING",
      "location": { "lat": 12.123, "lng": -86.123 }
    },
    ...
  ]
}
```

## 2. Stop Status Update
Action-based endpoints for transitioning stops through their lifecycle.

### Mark Arrival
- **URL**: `/api/operator/stops/{id}/arrive/`
- **Method**: `PATCH`
- **Success Response**: `200 OK`

### Record Completion (Success/Failure)
- **URL**: `/api/operator/stops/{id}/complete/`
- **Method**: `PATCH`
- **Payload**:
```json
{
  "status": "SUCCESS" | "FAILED",
  "notes": "Optional delivery notes"
}
```
- **Success Response**: `200 OK`

### Mark Departure
- **URL**: `/api/operator/stops/{id}/depart/`
- **Method**: `PATCH`
- **Success Response**: `200 OK`
