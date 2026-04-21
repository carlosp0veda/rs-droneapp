# Research Findings: Drone Delivery Run

## Technical Unknowns Resolved

### 1. Mapping Service Choice
- **Decision**: Use **Mapbox** with `react-map-gl`.
- **Rationale**: 
    - High performance for real-time tracking (WebGL based).
    - Superior customization for a premium "DroneApp" aesthetic.
    - Generous free tier for development.
- **Alternatives Considered**: 
    - **Leaflet**: Lightweight and free, but lacks the performance and modern look of Mapbox.
    - **Google Maps**: Industry standard with great data, but more expensive and less customizable.

### 2. Backend Geo-Spatial Extension
- **Decision**: Use **PostGIS** with Django's GeoDjango framework.
- **Rationale**: PostgreSQL is already the chosen database. PostGIS provides robust spatial querying for calculating distances and paths (e.g., flight path length).
- **Alternatives Considered**: Standard Latitude/Longitude fields without spatial indexing (inefficient for large runs).

### 3. Real-time Status Updates
- **Decision**: Use **Django Channels** and **WebSockets**.
- **Rationale**: For a "professional" feel (SC-001/SC-002), the operator view needs to reflect status changes immediately across the system.
- **Alternatives Considered**: Short polling (inefficient and potentially high latency).

### 4. Styling Strategy
- **Decision**: **Vanilla CSS** (as per project rules) with CSS Variables for the Design System tokens.
- **Rationale**: Provides maximum control over the "premium" look without the overhead/constraints of Tailwind or component libraries like shadcn.

## Dependency Analysis

| Category | Library | Purpose |
|----------|---------|---------|
| Backend | `django-geojson` | For easy GeoJSON serialization of locations |
| Backend | `djangorestframework-gis` | DRF integration for spatial data |
| Frontend | `react-map-gl` | React wrapper for Mapbox GL JS |
| Frontend | `lucide-react` | For high-quality, lightweight icons (markers/sidebar) |

## Implementation Patterns

### Map Pattern
- Use a central Map component that subscribes to the DeliveryRun state.
- Implement custom markers using HTML/CSS for Pickups vs. Deliveries.
- Plot the flight path using a GeoJSON `LineString`.

### Navigation List Pattern
- Sequenced list sidebar with high visual contrast for the "current" target.
- Use CSS transitions for status changes (Pending -> Arrived -> Complete).
