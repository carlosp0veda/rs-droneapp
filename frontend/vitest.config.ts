import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './src/test/setup.tsx',
    css: true,
    deps: {
      optimizer: {
        web: {
          include: ['react-map-gl/mapbox', 'mapbox-gl'],
        },
      },
    },
  },
})
