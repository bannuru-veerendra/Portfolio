"""
Portfolio Website - Main Application File

This module contains the Flask application setup and routing for the portfolio website.
"""

import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

from app import create_app

# Initialize the Flask application
app = create_app()

if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "0") == "1" or (
        os.getenv("FLASK_ENV", "production").lower() == "development"
    )
    host = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_RUN_PORT", "5000"))
    app.run(host=host, port=port, debug=debug)
