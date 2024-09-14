# Users and Tasks

This project provides user service to create and manage tasks.

## Project Structure
- `alembic/`:  contains the migrations for the database.

- `app/`: Contains the source code for the FastAPI application.
  - `api/`: Api user+tasks routes and controller.
  - `config/`: Configs required- database.
  - `middlewares/`: Auth middleware.
  - `models/`: ORM models for SQLAlchemy.
  - `schema/`: Pydantic schemas for request and response validation.
  - `services/`: Functions for user service and tasks service.
  - `main.py`: The entry point for the FastAPI application.

- `.env`: Environment variables for the application.

- `docker-compose.yml`: Docker Compose configuration for running the multi-container application.

- `Dockerfile`: Docker configuration file for building the application container.

- `requirements.txt`: List of Python package dependencies.


## Run Locally

1. **Clone the repository:**
    ```bash
    git clone https://github.com/anshulchhabra1991/UsersAndTasks.git
    cd UsersAndTasks
    ```

2. **Build and run the Docker containers:**
    ```bash
    docker-compose up --build
    ```

3. **Access the application:**
    The application will be available at `http://localhost:8333`.


## Sample Tokens
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbnNodWwiLCJ1c2VyX2lkIjoxLCJlbWFpbCI6ImFuc2h1bEBnbWFpbC5jb20iLCJleHAiOjE3MzQ5MTI0Mzl9.4MZqHtv0pN5RiTIauXnoyd1YI7PKhczmlv4VMQC56LE
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huIiwidXNlcl9pZCI6MiwiZW1haWwiOiJqb2huLmRvZUBleGFtcGxlLmNvbSIsImV4cCI6MTczNDkxMjQzOX0.gZsC5qTXV5w3_5n-d6d9IflsIT20I4Z4KYIgUmTCdWg
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqYW5lIiwidXNlcl9pZCI6MywiZW1haWwiOiJqYW5lLmRvZUBleGFtcGxlLmNvbSIsImV4cCI6MTczNDkxMjQzOX0.hE4VLIggYo5dgsNmxRZO0JWGbaBfvDGjZyoO7DMyfuo
```
