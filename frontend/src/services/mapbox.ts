export const MAPBOX_TOKEN = import.meta.env.VITE_MAPBOX_TOKEN;

if (!MAPBOX_TOKEN) {
  console.warn('Mapbox token is missing. Map components will not render correctly.');
}
