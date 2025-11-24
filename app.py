
import os
import google.generativeai as genai
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import markdown
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# In-memory rate limiting
request_counts = {}
RATE_LIMIT = 10  # requests
RATE_LIMIT_TIMEFRAME = timedelta(minutes=1)

@app.before_request
def rate_limit():
    ip_address = request.remote_addr
    now = datetime.now()

    if ip_address not in request_counts:
        request_counts[ip_address] = []

    # Remove requests outside the timeframe
    request_counts[ip_address] = [
        timestamp for timestamp in request_counts[ip_address]
        if now - timestamp < RATE_LIMIT_TIMEFRAME
    ]

    if len(request_counts[ip_address]) >= RATE_LIMIT:
        return jsonify({"error": "Rate limit exceeded. Please try again later."}), 429

    request_counts[ip_address].append(now)

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://cdn.jsdelivr.net; style-src 'self' https://cdn.jsdelivr.net"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/debug', methods=['POST'])
def debug():
    try:
        code = request.form['code']
        error_message = request.form['error_message']
        language = request.form['language']

        if not all([code, error_message, language]):
            return render_template('results.html', error="All fields are required.")

        prompt = f"""
        As an expert software engineer, provide a comprehensive analysis of the following code and its associated error. Your response should be professional, insightful, and formatted in clear, readable markdown.

        **Language:** `{language}`

        **Error Message / Stack Trace:**
        ```
        {error_message}
        ```

        **Code:**
        ```
        {code}
        ```

        ### In-Depth Analysis

        #### 1. **Root Cause Analysis**
        *   **What it is:** Concisely explain the direct cause of the error. What specific operation failed and why?
        *   **Why it happened:** Delve deeper. Explain the contextual programming mistake that led to this error (e.g., failure to validate input, incorrect algorithm, misunderstanding of a language feature).

        #### 2. **Debugging Flow**
        *   **Step-by-step thought process:** Outline the logical steps a developer would take to diagnose this issue. For example: "1. Examine the stack trace to find the failing line. 2. Inspect the variables at that line. 3. Realize variable `x` is `None` because..."

        #### 3. **Step-by-Step Fix**
        *   Provide a clear, numbered list of steps to correct the code. Be specific and actionable.

        #### 4. **Corrected Code**
        *   Present the complete, corrected code block. Use comments within the code to highlight the changes and explain the fix.

        #### 5. **Prevention & Best Practices**
        *   **General Principle:** Explain the programming principle or best practice that helps prevent this class of error (e.g., "Always validate external inputs," "Initialize variables before use").
        *   **Specific Recommendations:** Offer concrete, language-specific advice for avoiding this error in the future.
        """

        model = genai.GenerativeModel('gemini-pro-latest')
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.2
            ),
            safety_settings=[
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
            ]
        )

        html_response = markdown.markdown(response.text, extensions=['fenced_code'])

        return render_template('results.html', results=html_response)

    except Exception as e:
        return render_template('results.html', error=f"An unexpected error occurred: {e}")

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
