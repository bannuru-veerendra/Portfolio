"""
Portfolio - Flask Application Factory

This module contains the Flask application factory function for the portfolio website.
"""

from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route('/')
    def index():
        """Home page route handler."""
        return "Portfolio backend is running"

    return app
