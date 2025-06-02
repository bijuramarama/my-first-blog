#!/bin/bash

# Start Gunicorn
# Gunicorn will bind to port 5000, which Nginx is configured to proxy to.
echo "Starting Gunicorn..."
gunicorn --workers 3 --bind 0.0.0.0:5000 app:app --daemon

# Start Nginx in the foreground
echo "Starting Nginx..."
nginx -g 'daemon off;'
