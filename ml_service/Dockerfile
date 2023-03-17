# Start with an official Python runtime as a parent image
FROM python:3.11-slim

# Set environmental variables
ENV PYTHONUNBUFFERED=true

# Set the working directory in the container
WORKDIR /code

# Copy poetry files
COPY pyproject.toml poetry.lock /code/

# Install poetry and project dependencies
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root --without dev

# Copy the project files into the container
COPY . /code
