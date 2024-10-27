# Don't use -slim as it has issues
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Install dependencies
# Probably a could do this more dynically with the pip freeze.
# I can't find any other way to make this work
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

