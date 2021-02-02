# Dockerfile | Cannlytics API
# Created: 2/1/2021

# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster
# Use the official lightweight Python image.
# https://hub.docker.com/_/python
# FROM python:3.9-slim

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8080

# Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE 1

# Setting this ensures that print statements and log messages
# promptly appear in Cloud Logging.
ENV PYTHONUNBUFFERED True

# Install dependencies.
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Specificy directory.
ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy local code to the container image.
COPY . ./

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
# RUN useradd appuser && chown -R appuser /app
# USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder:cannlytics. Please enter the Python path to wsgi file.
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonPath.to.wsgi"]

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# See:
# https://docs.gunicorn.org/en/stable/design.html#how-many-workers
# https://docs.gunicorn.org/en/stable/design.html#how-many-threads
CMD exec gunicorn --bind :$PORT --workers 3 --threads 8 --timeout 0 cannlytics_api.wsgi:application
