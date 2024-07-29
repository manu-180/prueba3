# This Dockerfile is used to deploy a simple single-container Reflex app instance.
FROM python:3.12

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .

COPY .env .env

RUN pip install -r requirements.txt

# Deploy templates and prepare app
RUN reflex init

# Download all npm dependencies and compile frontend
RUN reflex export --frontend-only --no-zip

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

# Always apply migrations before starting the backend.
CMD [ -d alembic ] && reflex db migrate; reflex run --env prod