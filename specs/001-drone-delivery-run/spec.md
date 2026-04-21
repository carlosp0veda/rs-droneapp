# Feature Specification: Drone Delivery Run

**Feature Branch**: `001-drone-delivery-run`  
**Created**: 2026-04-20  
**Status**: Draft  
**Input**: User description: "Build a web app that gives a professional flying drone operator a view of where to go to make their delivery run. A typical delivery run consists of multiple pickup locations (from restaurants) and multiple delivery locations (to residential addresses)."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Delivery Run Overview (Priority: P1)

As a drone operator, I want to see an overview of my entire delivery run so that I can plan my energy usage and flight path before takeoff.

**Why this priority**: Essential for flight safety and planning. Without the overview, the operator cannot verify the safety of the entire route.

**Independent Test**: Can be tested by loading a sample delivery run and verifying that the total number of pickups and deliveries matches the source data.

**Acceptance Scenarios**:
1. **Given** a delivery run with 2 pickups and 3 deliveries, **When** I open the dashboard, **Then** I should see all 5 locations listed in correctly sequenced order.
2. **Given** a delivery run, **When** I view the map, **Then** I should see a connected path between all pickup and delivery coordinates.

---

### User Story 2 - Pickup Execution (Priority: P2)

As a drone operator, I want to specifically identify and navigate to restaurant pickup locations so that I can collect the packages accurately.

**Why this priority**: Critical path for fulfillment. Pickups must happen before any deliveries can be made.

**Independent Test**: Can be tested by filtering the location list for "Pickup" types and verifying the location metadata (Restaurant Name).

**Acceptance Scenarios**:
1. **Given** I am at a pickup location, **When** I mark the pickup as "Arrived", **Then** the UI should highlight the specific restaurant details.
2. **Given** an active pickup, **When** I mark it as "Complete", **Then** the system should automatically point me to the next location in the sequence.

---

### User Story 3 - Residential Delivery (Priority: P2)

As a drone operator, I want to identify residential delivery locations and their specific drop-off instructions so that I can complete the delivery run successfully.

**Why this priority**: Final step of the value chain. Requires clear distinction from restaurant locations.

**Independent Test**: Can be tested by navigating to a "Delivery" location and verifying that residential address format is displayed.

**Acceptance Scenarios**:
1. **Given** a delivery location, **When** I reach the coordinate, **Then** the UI should show drop-off notes (e.g., "Backyard", "Landing Pad B").
2. **Given** a completed delivery, **When** I mark it as "Delivered", **Then** the location should be visually dimmed or checked off in the list.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST display an interactive map with markers for all locations.
- **FR-002**: System MUST display a sequenced location list sidebar.
- **FR-003**: System MUST visually differentiate between "Pickup" (Restaurant) and "Delivery" (Residential) markers.
- **FR-002**: System MUST provide a mechanism to change the status of a location (Pending, Arrived, Complete).
- **FR-005**: System MUST support runs with multiple pickup locations (from restaurants) and multiple delivery locations (to residential addresses).

### Key Entities

- **Operator**: The professional drone pilot (License number, certification, active status).
- **DeliveryRun**: Container for the entire journey; includes status, operator ID, and estimated duration.
- **Location**: An individual point in the run sequence.
    - `type`: ENUM (PICKUP, DELIVERY)
    - `locationName`: String (e.g., "Joe's Pizza" or "123 Main St")
    - `coordinates`: [Lat, Lng]
    - `status`: ENUM (PENDING, ARRIVED, COMPLETED)
- **Order**: Metadata associated with each location (Customer name, items, drop-off notes).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Operator can identify the next location type (Pickup/Delivery) in under 1 second of visual inspection.
- **SC-002**: Map TTI (Time to Interactive) MUST be under 2 seconds for runs with up to 20 locations.
- **SC-003**: 100% adherence to DroneApp Design System tokens and WCAG 2.1 Level AA compliance.
- **SC-002**: System MUST handle at least 5 pickups and 10 deliveries in a single run without degradation in UI performance.

## Assumptions

- **A-001**: Mapping data is provided via a standard technology-agnostic tile service.
- **A-002**: Real-time telemetry (altitude, battery) is OUT OF SCOPE for this view (per user confirmation).
- **A-003**: The sequence of locations is pre-calculated by a backend optimization engine; this app is for visualization and execution only.
