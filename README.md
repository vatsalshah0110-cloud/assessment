Project Structure:

assessment/
--- app.py                  # Main Flask application with two routes
--- requirements.txt        # Python dependencies (Flask and Redis)
--- Dockerfile              # Dockerfile for the Flask web app
--- docker-compose.yaml     #  Al three services together
--- build.sh                # Script to build and start all containers
--- start.sh                # Script to start containers
--- down.sh                 # Script to stop and remove containers
--- .gitignore              # Ignores pycache and .pyc files
--- nginx/
    --- Dockerfile          # Dockerfile for the Nginx static server
    --- index.html          # Static HTML page served by Nginx

Services Overview:

web :
 - base image : python:3.12-slim
 - port mapping : 5000:5000
 - role: flask application

redis:
 - base image : redis:alpine
 - role: used as a counter for how many times the page has been visited

nginx:
 - base image: nginx:alpine
 - port mapping: 80:80
 - role: used as a static html content server

All three services run on a shared Docker bridge network called 'assessment' done in the docker compose file

Shell Script:

-- to make the scripts executable: 'chmod +x script-name'

build.sh :
 - command - ./build.sh
 - what it does: docker compose up --build

start.sh :
 - command - ./start.sh
 - what it does: stars container without rebuilding

down.sh :
 - command - ./down.sh
 - what it does: stops and removes all containers



Accessing the application:

nginx: http://localhost/
flask app : http://localhost:5000
flask app with counter : http://localhost:5000/counter


How It Works:

The Flask app has two routes. The / route returns a simple text response. 

The /counter route connects to Redis and increments a counter every time the page is visited, showing the total visit count.

Redis connection details (REDIS_HOST, REDIS_PORT) are passed as environment variables in the Compose file, so the Flask app doesn't have hardcoded values.

The Nginx container serves a static index.html page that guides visitors to the Flask routes.
