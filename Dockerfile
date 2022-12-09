FROM python:3.7.15-alpine

# Copy Requirements file
COPY ./requirements.txt /tmp

# Install Python dependencies
RUN pip install --no-cache-dir -r /tmp/requirements.txt
