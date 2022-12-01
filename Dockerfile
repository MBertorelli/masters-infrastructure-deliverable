FROM python:3.7.15-alpine

# Copy Requirements file
COPY ./requirements.txt /tmp/

# Install Python dependencies
RUN pip install -r /tmp/requirements.txt

# Copy Application Source Code
COPY ./app /app

WORKDIR /app

# Run server
CMD uvicorn main:app --reload --host 0.0.0.0
