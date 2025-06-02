# Task Manager API

This is a simple Flask-based Task Manager API used for testing AI model performance on code editing tasks. It supports basic CRUD operations on in-memory tasks.

## Features

- `GET /tasks` — List all tasks
- `POST /tasks` — Create a new task (requires `title`)
- `PUT /tasks/<id>` — Fully update a task by ID (requires `title`)
- `DELETE /tasks/<id>` — Delete a task by ID

> The PATCH method is not yet implemented in the pre-edit version.

---

## Running Tests in Docker

### 1. Build the Docker image
```bash
./build_docker.sh task-api
docker run --rm task-api ./run_tests.sh
