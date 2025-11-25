# AI-Powered Code Debugger

[![GitHub stars](https://img.shields.io/github/stars/your-username/your-repo.svg?style=social)]([https://github.com/your-username/your-repo](https://github.com/ayushdubey570/ai-code-debugger))
[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Flask Version](https://img.shields.io/badge/flask-2.2.2-blue.svg)](https://flask.palletsprojects.com/en/2.2.x/)

An intelligent web-based tool that leverages the power of Google's Gemini AI to help developers debug their code more efficiently. This application provides a user-friendly interface to submit code snippets and error messages, and in return, it offers a detailed analysis, a step-by-step solution, and best practices to prevent similar issues.

## Features

-   **Multi-Language Support:** Analyzes code in Python, JavaScript, Java, and C++.
-   **In-Depth Analysis:** Provides a root cause analysis to explain *why* an error occurs.
-   **Step-by-Step Solutions:** Delivers clear, actionable steps to fix the code.
-   **User-Friendly Interface:** A clean and intuitive web interface for a smooth user experience.

## Technology Stack

-   **Backend:** Python, Flask
-   **AI Model:** Google Gemini
-   **Frontend:** HTML, CSS, JavaScript
-   **Deployment:** Docker (Optional)

## Local Development Setup

Follow these steps to set up the project for local development.

### 1. Clone the Repository

```bash
git clone https://github.com/ayushdubey570/ai-code-debugger.git
cd your-repo
```

### 2. Set Up the Environment

Create a `.env` file in the root of the project and add your Gemini API key.

```bash
cp .env.example .env
```

Now, open the `.env` file and add your API key:

```
GEMINI_API_KEY=your_api_key_here
```

### 3. Install Dependencies

It is recommended to use a virtual environment to manage the project's dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Run the Application

Once the dependencies are installed, you can run the application using the following command:

```bash
python3 app.py
```

The application will be available at `http://127.0.0.1:5000`.

## Docker Setup (Optional)

This project includes a `Dockerfile` for easy containerization.

### 1. Build the Docker Image

```bash
docker build -t ai-debugger .
```

### 2. Run the Docker Container

```bash
docker run -p 5000:5000 -e GEMINI_API_KEY=your_api_key_here ai-debugger
```

The application will be available at `http://127.0.0.1:5000`.

## Project Structure

-   `app.py`: The main Flask application file.
-   `templates/`: Contains the HTML templates for the web pages.
-   `static/`: Contains the static files (CSS, JavaScript, images).
-   `Dockerfile`: For building the Docker image.
-   `requirements.txt`: The list of Python dependencies.
-   `.env.example`: An example file for the environment variables.
  
##Demo?Screenshots
<img width="1422" height="822" alt="Screenshot 2025-11-24 at 22-14-54 AI Debugger" src="https://github.com/user-attachments/assets/0ce959a5-298c-45c2-8b66-fa09330932a1" />
<img width="1422" height="3361" alt="Screenshot 2025-11-24 at 22-16-34 AI Debugger" src="https://github.com/user-attachments/assets/5473f9c9-b4f1-4202-b249-4b1285c874ca" />


https://github.com/user-attachments/assets/1cd304c9-6477-46c6-9711-a19ee7bacc81



