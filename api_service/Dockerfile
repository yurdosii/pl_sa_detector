# Start with an official Python runtime as a parent image
FROM python:3.11-slim

# Set environmental variables
ENV PYTHONUNBUFFERED=true

# Set the working directory in the container
WORKDIR /code

# Copy the project files into the container
COPY . /code

# Install poetry and project dependencies
RUN pip install poetry && poetry install --no-root --without dev

# Expose the port number that the application will listen on
EXPOSE 8000

# Start the server with uvicorn
CMD ["poetry", "run", "uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
