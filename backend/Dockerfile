# Use Python 3.12.3 on Alpine 3.19 as the base image
FROM python:3.12.3-alpine3.19

# Set the working directory in the container
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install dependencies
# gcc and musl-dev are required to build some Python packages
RUN apk add --no-cache gcc musl-dev

# Copy the requirements file into the container
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements-dev.txt /tmp/requirements-dev.txt

# Overritten in docker-compose.yml
ARG DEV=false 

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    if [ $DEV = "true" ]; then pip install -r /tmp/requirements-dev.txt; fi && \
    rm -rf /tmp

# Copy the rest of your application code
COPY . ./app

# Expose the port that the application runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]