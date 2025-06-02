# Flask MongoDB Nginx Docker Application

This application provides a simple user login system using Flask, MongoDB, and Nginx, all containerized with Docker.

## Prerequisites

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/) (usually included with Docker Desktop)

## Project Structure

```
flask_mongo_nginx_docker_app/
├── Dockerfile            # Defines the application container environment
├── docker-compose.yml    # Orchestrates the app, mongo, and nginx services
├── nginx.conf            # Nginx configuration
├── requirements.txt      # Python dependencies
├── start.sh              # Script to start Gunicorn and Nginx
├── app.py                # Flask application logic
├── templates/            # HTML templates
│   ├── login.html
│   └── index.html
└── README.md             # This file
```

## Setup and Running the Application

1.  **Clone the repository or ensure you have all the files in a directory named `flask_mongo_nginx_docker_app`.**

2.  **Navigate to the project directory:**
    ```bash
    cd flask_mongo_nginx_docker_app
    ```

3.  **Build and run the application using Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    This command will:
    *   Build the Docker image for the application based on the `Dockerfile`.
    *   Start the `app` service (Flask/Nginx) and the `mongo` service.
    *   Create a volume `mongo_data` for persistent MongoDB storage.

4.  **Access the application:**
    Open your web browser and go to [http://localhost:80](http://localhost:80). You should see the login page.

## Default Login Credentials

For testing purposes, you can log in with:
*   **Username:** `testuser`
*   **Password:** `testpass`

If the user "testuser" does not exist, the application will create it upon the first successful login attempt with these credentials. This is for demonstration purposes only and not suitable for production.

## Stopping the Application

To stop the application, press `Ctrl+C` in the terminal where `docker-compose up` is running.

To stop and remove the containers, network, and volumes (including the MongoDB data unless you want to preserve it):
```bash
docker-compose down
```
To remove the MongoDB data volume as well:
```bash
docker-compose down -v
```

## Notes

*   The Flask application runs in development mode by default (`FLASK_ENV=development`). Change this in `docker-compose.yml` for production.
*   Passwords are currently stored in plaintext in MongoDB. **This is highly insecure and should never be done in a production environment.** Use password hashing (e.g., with Werkzeug's security helpers or libraries like passlib) in a real application.
*   The `start.sh` script starts Gunicorn in daemon mode and then Nginx in the foreground. Ensure Gunicorn is properly configured for your needs (e.g., number of workers).
