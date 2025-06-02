# Start with a Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends     nginx     # MongoDB will be run as a separate container using docker-compose
    # but we might need mongo-tools or similar client utilities in the app container later.
    # For now, we'll skip direct MongoDB installation in this Dockerfile
    # as it's better to link it via docker-compose.
    # If specific mongo client tools are needed, they can be added.
 && apt-get clean  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

COPY ./nginx.conf /etc/nginx/nginx.conf

# Expose ports (Nginx will listen on 80)
EXPOSE 80

# Command to run Nginx and Gunicorn (or a simple Flask dev server for now)
# This will be refined later, potentially with a startup script.
# For now, Nginx needs to be configured and started.
# Flask app will be started by Gunicorn or similar.
COPY ./start.sh /start.sh
CMD ["/start.sh"]
