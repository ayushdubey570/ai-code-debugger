# Flask Debugging Helper for Google Cloud Run

This project is a Flask web application that helps developers debug code using Google's Gemini LLM. It's designed to be deployed to Google Cloud Run as a single container.

## Features

- **Backend API**: A Flask-based API that takes code, an error message, and a programming language, and returns a debugging analysis from the Gemini API.
- **Frontend UI**: A simple, mobile-responsive web interface for submitting code and viewing the debugging results.
- **Google Cloud Run Ready**: Optimized for deployment on Google Cloud Run, including a `Dockerfile` and `gunicorn` for serving the application.

## Getting Started

### Prerequisites

- Python 3.11
- Google Cloud SDK
- A Google Cloud project with the Cloud Run and Cloud Build APIs enabled.
- A Gemini API key from Google AI Studio.

### Local Development

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/debugging-helper.git
   cd debugging-helper
   ```

2. **Create a virtual environment and install dependencies:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Create a `.env` file:**

   Create a `.env` file in the root of the project and add your Gemini API key:

   ```
   GEMINI_API_KEY=your_gemini_key_here
   ```

4. **Run the application:**

   ```bash
   python app.py
   ```

   The application will be available at `http://localhost:8080`.

## Deployment to Google Cloud Run

1. **Build and deploy the application:**

   Replace `YOUR_PROJECT_ID` with your Google Cloud project ID.

   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/debugger-app
   gcloud run deploy debugger-app \
     --image gcr.io/YOUR_PROJECT_ID/debugger-app \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars=GEMINI_API_KEY=your_gemini_key_here \
     --port=8080
   ```

2. **Access the deployed application:**

   The command will output the URL of your deployed application.

## Cost Optimization

- **Minimum Instances**: To minimize costs, set the minimum number of instances to 0. This will allow the application to scale to zero when not in use.
- **Request Timeout**: Adjust the request timeout to a reasonable value to avoid long-running requests from incurring unnecessary costs.

## Troubleshooting

- **502 Bad Gateway**: This error can occur if the application fails to start. Check the logs in the Google Cloud Console for more information.
- **Rate Limiting**: The application has a simple in-memory rate limit of 10 requests per minute per IP address. If you exceed this limit, you will receive a `429 Too Many Requests` error.
- **Invalid API Key**: If you provide an invalid Gemini API key, you will see an error message in the application.
