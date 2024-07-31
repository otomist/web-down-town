# Use an official Python runtime as a parent image
FROM python:3.12.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app /app/

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV PORT=8080

# Run server.py when the container launches
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]
