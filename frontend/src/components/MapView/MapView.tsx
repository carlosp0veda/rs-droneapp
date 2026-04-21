import { FC } from 'react';
import Map, { Marker, NavigationControl } from 'react-map-gl/mapbox';
import 'mapbox-gl/dist/mapbox-gl.css';
import { MAPBOX_TOKEN } from '../../services/mapbox';

interface Location {
  id: string;
  name: string;
  category: string;
  coordinates: {
    latitude: number;
    longitude: number;
  };
  status: string;
}

interface MapViewProps {
  locations: Location[];
}

const MapView: FC<MapViewProps> = ({ locations }) => {
  return (
    <div style={{ width: '100%', height: '100%', borderRadius: 'var(--radius)', overflow: 'hidden' }}>
      <Map
        initialViewState={{
          longitude: -74.006,
          latitude: 40.7128,
          zoom: 12
        }}
        mapStyle="mapbox://styles/mapbox/streets-v12"
        mapboxAccessToken={MAPBOX_TOKEN}
      >
        <NavigationControl position="top-right" />
        
        {locations.map((loc) => (
          <Marker
            key={loc.id}
            longitude={loc.coordinates.longitude}
            latitude={loc.coordinates.latitude}
            anchor="bottom"
          >
            <div 
              className={`marker marker-${loc.category.toLowerCase()} ${loc.status === 'COMPLETED' ? 'marker-completed' : ''}`}
              data-testid={`marker-${loc.category.toLowerCase()}-${loc.id}`}
              title={`${loc.name} (${loc.category})`}
            >
              {loc.category === 'PICKUP' ? 'P' : 'D'}
            </div>
          </Marker>
        ))}
      </Map>
    </div>
  );
};

export default MapView;
