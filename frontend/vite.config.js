import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
      proxy: {
        // Proxy all /api requests to backend
        '/api': {
          target: 'http://localhost:8070',
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, '') // Remove /api prefix
        }
      }
    }
})
