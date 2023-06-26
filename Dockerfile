# Dockerfile in the root of the second repository

# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory
WORKDIR /usr/src/app

# Install pipenv
RUN pip install pipenv

# Copy the Pipfile and Pipfile.lock to the working directory
COPY Pipfile Pipfile.lock ./

# Install the project dependencies
RUN pipenv install

# Copy the rest of the code
COPY . .

# The command to run the application
CMD ["pipenv", "run", "watch"]
