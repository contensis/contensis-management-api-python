FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Install uv for everyone not just the current user.
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
 && cp /root/.local/bin/uv /usr/local/bin/uv

# Label the image so it looks better on Github.
LABEL org.opencontainers.image.source=https://github.com/contensis/contensis-management-api-python/
LABEL org.opencontainers.image.description="contensis-management-api-python development container."
