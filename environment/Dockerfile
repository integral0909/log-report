FROM public.ecr.aws/docker/library/python:3.13-slim-bookworm@sha256:01f42367a0a94ad4bc17111776fd66e3500c1d87c15bbd6055b7371d39c124fb

# Test dependencies are baked into this single image (pinned); test.sh installs nothing.
RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

# Pre-create the parent dir of the output path the agent writes.
RUN mkdir -p /app
WORKDIR /app

# Seed input only. The reference solution and tests are never copied into the image.
COPY access.log /app/access.log
