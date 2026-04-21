# Data Model: Drone Delivery Run

## Entity Overview

The system architecture follows a decoupled model where the Backend manages spatial data and run state, while the Frontend visualizes these entities.

```mermaid
erDiagram
    OPERATOR ||--o{ DELIVERY_RUN : manages
    DELIVERY_RUN ||--|{ LOCATION : contains
    LOCATION ||--|| ORDER : associated_with

    OPERATOR {
        UUID id PK
        string license_number
        string certification_level
        boolean is_active
    }

    DELIVERY_RUN {
        UUID id PK
        UUID operator_id FK
        string status "ENUM(PLANNING, IN_PROGRESS, COMPLETED)"
        timestamp started_at
        timestamp completed_at
        jsonb metadata "estimated_duration, total_distance"
    }

    LOCATION {
        UUID id PK
        UUID run_id FK
        integer sequence_order
        string category "ENUM(PICKUP, DELIVERY)"
        Point coordinates "PostGIS PointField"
        string name "Restaurant or Address"
        string status "ENUM(PENDING, ARRIVED, COMPLETED)"
    }

    ORDER {
        UUID id PK
        UUID location_id FK
        string customer_name
        jsonb items
        text instructions "Drop-off notes"
    }
```

## Schema Details

### 1. DeliveryRun
- **Description**: The top-level container for a journey.
- **Constraints**: 
    - At least 1 Location required.
    - End time must be after start time.

### 2. Location
- **Description**: A waypoint in the run.
- **Field Details**:
    - `coordinates`: Django `PointField` (SRID 4326).
    - `sequence_order`: Determines the flight path connectivity.
- **Validation**:
    - `PICKUP` locations should generally precede `DELIVERY` locations for the same order (though not strictly enforced for multi-pickup runs).

### 3. Order
- **Description**: Delivery metadata.
- **Field Details**:
    - `instructions`: Essential for Residential deliveries (FR-003/Story 3).

## State Transitions

### DeliveryRun State
- `PLANNING` -> `IN_PROGRESS` (on takeoff/start)
- `IN_PROGRESS` -> `COMPLETED` (when all locations are COMPLETED)

### Location State
- `PENDING` -> `ARRIVED` (when drone reaches geofence/manual toggle)
- `ARRIVED` -> `COMPLETED` (on pickup/drop-off confirmation)
