#!/bin/bash
cd project1
alembic upgrade head
poetry run uvicorn main:app --host 0.0.0.0 --port 8000