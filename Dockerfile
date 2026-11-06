
# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends git perl && \
    rm -rf /var/lib/apt/lists/*

# Copy the project into the container
COPY . /app

# Make the entrypoint script executable
RUN chmod +x /app/.github/scripts/entrypoint.sh

# Execute the entrypoint script
ENTRYPOINT ["/bin/bash", "/app/.github/scripts/entrypoint.sh"]
