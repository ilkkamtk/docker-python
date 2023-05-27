FROM python:3.9-alpine3.18
# Set the working directory
WORKDIR /app

# Copy your application code into the container
COPY app/. /app/
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh

# Set the entrypoint script as executable
RUN chmod +x /entrypoint.sh

# Set the entrypoint command
ENTRYPOINT ["/entrypoint.sh"]