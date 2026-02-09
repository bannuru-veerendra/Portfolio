"""
Application Configuration

Centralized configuration management for the portfolio application.
"""

import os

from dotenv import load_dotenv

# Load .env before reading any env vars so Config sees them on first import
load_dotenv()


class Config:
    """Base configuration class for the Flask application."""

    # Flask configuration
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG: bool = os.getenv('FLASK_ENV', 'development').lower() != 'production'

    # Logging configuration
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO').upper()