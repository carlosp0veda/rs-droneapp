# Research: Drone Operator Delivery Flow

## Goal
Determine the best technical approach for the operator flow, focusing on map integration, offline support, and data synchronization.

## Findings

### Map Integration
**Decision**: Use `react-leaflet` for map visualization.
**Rationale**: 
- Lightweight and highly customizable.
- Pairs well with `djangorestframework-gis` on the backend.
- Supports high-contrast themes (important for high-glare environments mentioned in SC-002).
**Alternatives**: 
- Mapbox: More powerful but requires API keys and has a heavier footprint.
- Google Maps: Licensing costs and requires external script loading.

### Offline Support & State Management
**Decision**: Use `Zustand` for local state and `IndexedDB` (via `idb-keyval`) for persistent offline buffering.
**Rationale**:
- Zustand is performant and easy to use with React.
- `IndexedDB` handles larger data sets and is more robust than `LocalStorage` for transactional status updates.
- Background sync will be implemented by checking the buffer on app start or network recovery.

### Geolocation Strategy
**Decision**: Use the standard Browser Geolocation API with `watchPosition`.
**Rationale**: 
- Provides real-time tracking of the operator's movement.
- Native support in all modern mobile browsers.

### API Architecture
**Decision**: RESTful endpoints with specific status transition actions.
**Rationale**:
- Aligns with the existing DRF backend.
- Using `PATCH` for state transitions ([Assigned -> Arrived -> Success/Failure -> Departed]) keeps the interface clean.

## Unresolved Questions
None. The tech stack and requirements are well-aligned with the existing codebase.
