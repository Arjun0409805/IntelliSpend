## Running IntelliSpendAI with Docker

This project provides a full Docker-based setup for both the Python backend (FastAPI), the static JavaScript frontend, and a PostgreSQL database. The configuration is managed via `docker-compose` and custom Dockerfiles for each service.

### Project-Specific Docker Requirements

- **Python Backend**
  - Uses `python:3.9-slim` as the base image
  - Installs system dependencies for packages like `sentence-transformers` and `prophet`
  - Runs the FastAPI app with `uvicorn` on port **8000**
  - Requires a `.env` file at `IntelliSpendAI/.env` with at least `DATABASE_URL` and any required API keys

- **Frontend**
  - Uses `node:20-alpine` as the base image
  - Serves static files (`index.html`, `app.js`, `styles.css`) using the `serve` package
  - Runs on port **8080**
  - No environment variables required

- **PostgreSQL Database**
  - Uses the official `postgres:latest` image
  - Exposes port **5432**
  - Environment variables set in `docker-compose.yml`:
    - `POSTGRES_DB=intellispends`
    - `POSTGRES_USER=user`
    - `POSTGRES_PASSWORD=password`
  - Data is persisted in a Docker volume (`pgdata`)
  - **Note:** The `pgvector` extension must be enabled in the database after startup

### Required Environment Variables

- **Backend**: Place a `.env` file in `IntelliSpendAI/.env` with at least:
  - `DATABASE_URL` (connection string for PostgreSQL)
  - Any API keys required by your application
- **Frontend**: No environment variables required
- **Database**: Credentials are set in `docker-compose.yml` (see above)

### Build and Run Instructions

1. **Ensure your `.env` file is present:**
   - Copy or create `IntelliSpendAI/.env` with the required variables before building.

2. **Build and start all services:**
   ```sh
   docker compose up --build
   ```
   This will build the backend and frontend images and start all three services (backend, frontend, database).

3. **Access the services:**
   - **Backend API:** http://localhost:8000
   - **Frontend:** http://localhost:8080
   - **PostgreSQL:** localhost:5432 (use credentials from `docker-compose.yml`)

4. **Enable `pgvector` extension in PostgreSQL:**
   After the database container is running, connect to the database and run:
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   ```

### Ports Used

- **Backend (FastAPI):** 8000
- **Frontend (Static):** 8080
- **PostgreSQL:** 5432

### Special Configuration

- The backend expects a `.env` file with the correct `DATABASE_URL` and any API keys.
- The `pgvector` extension must be enabled manually in the PostgreSQL database after the first run.
- All services are connected via the `intellispend-net` Docker network for internal communication.

---

*This section was updated to reflect the current Docker-based setup for IntelliSpendAI. Please ensure your environment variables and database extensions are configured as described above for a successful deployment.*
