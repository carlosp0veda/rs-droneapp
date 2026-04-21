import { render, screen } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import MapView from './MapView';

vi.mock('mapbox-gl', () => ({
  Map: vi.fn(),
  NavigationControl: vi.fn(),
}));

vi.mock('react-map-gl/mapbox', () => ({
  Map: ({ children }: { children: React.ReactNode }) => <div data-testid="map-container">{children}</div>,
  Marker: ({ children }: { children: React.ReactNode }) => <div data-testid="map-marker">{children}</div>,
  NavigationControl: () => <div data-testid="map-navigation" />,
  Source: ({ children }: { children: React.ReactNode }) => <>{children}</>,
  Layer: () => null,
}));

describe('MapView', () => {
  const mockLocations = [
    {
      id: '1',
      name: "Joe's Pizza",
      category: 'PICKUP',
      coordinates: { latitude: 40.7128, longitude: -74.0060 },
      status: 'PENDING',
    },
    {
      id: '2',
      name: "Alice's Home",
      category: 'DELIVERY',
      coordinates: { latitude: 40.7130, longitude: -74.0050 },
      status: 'PENDING',
    }
  ];

  it('renders all markers for given locations', () => {
    try {
      render(<MapView locations={mockLocations} />);
    } catch (e) {
      console.error("RENDER ERROR:", e);
      throw e;
    }
    
    // Check if markers are rendered using alt text or specific IDs
    expect(screen.getByTestId('marker-pickup-1')).toBeInTheDocument();
    expect(screen.getByTestId('marker-delivery-2')).toBeInTheDocument();
  });
});
