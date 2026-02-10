"""
Portfolio - Flask Application Factory

This module contains the Flask application factory function for the portfolio website.
"""

import os

from flask import Flask
from app.config import Config
from app.routes.index import index_bp
from app.logger import setup_logging


def create_app() -> Flask:
    """Create and configure the Flask application instance."""

    app = Flask(__name__)
    app.config.from_object(Config)

    setup_logging(app)
    # Only log in the worker that serves (avoid duplicate when Flask reloader runs two processes)
    if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        app.logger.info(
            "Application started (DEBUG=%s, LOG_LEVEL=%s)",
            app.config.get("DEBUG"),
            app.config.get("LOG_LEVEL", "INFO"),
        )

    app.register_blueprint(index_bp)

    return app
