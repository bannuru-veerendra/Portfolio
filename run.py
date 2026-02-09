"""
Portfolio Website - Main Application File

This module contains the Flask application setup and routing for the portfolio website.
"""

from app import create_app

# Initialize the Flask application
app = create_app()

# Run the application in debug mode for development
if __name__ == "__main__":
    app.run(debug=True)
