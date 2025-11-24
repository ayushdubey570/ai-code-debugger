# ---- Base Stage ----
FROM python:3.10-slim as base

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Production Stage ----
FROM base as production

# Set a non-root user
RUN useradd --create-home appuser
USER appuser
WORKDIR /home/appuser/app

# Copy the application code
COPY . .

# Set the Gunicorn command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
