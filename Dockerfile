FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create a non-root user and switch to it
RUN useradd --create-home nonroot
USER nonroot

# Set environment variables
ENV PORT 8080
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# Expose the port the app runs on
EXPOSE 8080

# Run the application using Gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
