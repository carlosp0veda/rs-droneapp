import '@testing-library/jest-dom';
import { vi } from 'vitest';

// Mock mapbox-gl and react-map-gl
vi.mock('mapbox-gl', () => ({
  Map: vi.fn(),
  NavigationControl: vi.fn(),
}));

vi.mock('react-map-gl/mapbox', () => ({
  Map: ({ children }: { children: node_placeholder }) => <div data-testid="map-container">{children}</div>,
  Marker: ({ children }: { children: node_placeholder }) => <div data-testid="map-marker">{children}</div>,
  NavigationControl: () => <div data-testid="map-navigation" />,
  Source: ({ children }: { children: node_placeholder }) => <>{children}</>,
  Layer: () => null,
}));
