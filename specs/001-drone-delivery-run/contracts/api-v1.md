# API Contracts: Drone Delivery Run

## Overview
All endpoints are relative to `/api/v1/`. Authentication is required for all endpoints (JWT assumed).

## Delivery Runs

### GET `/delivery-runs/`
- **Description**: List all delivery runs for the authenticated operator.
- **Response**:
    ```json
    [
      {
        "id": "uuid",
        "status": "PLANNING|IN_PROGRESS|COMPLETED",
        "started_at": "timestamp",
        "total_locations": 5
      }
    ]
    ```

### GET `/delivery-runs/{id}/`
- **Description**: Detailed view of a specific run, including sequenced locations.
- **Response**:
    ```json
    {
      "id": "uuid",
      "status": "IN_PROGRESS",
      "locations": [
        {
          "id": "uuid",
          "sequence_order": 1,
          "category": "PICKUP",
          "name": "Joe's Pizza",
          "coordinates": {
            "latitude": 40.7128,
            "longitude": -74.0060
          },
          "status": "COMPLETED",
          "order": {
            "customer_name": "Alice Smith",
            "instructions": "Wait at side door"
          }
        },
        ...
      ]
    }
    ```

### PATCH `/locations/{id}/`
- **Description**: Update location status (Arrived/Completed).
- **Request**:
    ```json
    {
      "status": "ARRIVED"
    }
    ```
- **Response**: `200 OK` with updated location object.

## WebSockets

### Endpoint: `ws://{host}/ws/delivery/{run_id}/`
- **Event: `status_update`**
    - **Trigger**: When a location or run status changes.
    - **Payload**:
        ```json
        {
          "type": "location_update",
          "location_id": "uuid",
          "new_status": "COMPLETED",
          "updated_at": "timestamp"
        }
        ```
