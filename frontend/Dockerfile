FROM node:20-alpine

# Install pnpm
RUN npm install -g pnpm

WORKDIR /app

# Copy lockfile and package.json to leverage Docker cache
COPY pnpm-lock.yaml package.json ./

# Install dependencies before copying source
RUN pnpm install

# Copy source code
COPY . .

# Expose Vite's default dev port
EXPOSE 5173

# Run Vite in host mode
CMD ["pnpm", "dev", "--host"]
