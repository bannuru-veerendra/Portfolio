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

    # Contact Form Validation
    MAX_NAME_LENGTH: int = int(os.getenv('MAX_NAME_LENGTH', '100'))
    MAX_EMAIL_LENGTH: int = int(os.getenv('MAX_EMAIL_LENGTH', '254'))
    MAX_SUBJECT_LENGTH: int = int(os.getenv('MAX_SUBJECT_LENGTH', '200'))
    MAX_MESSAGE_LENGTH: int = int(os.getenv('MAX_MESSAGE_LENGTH', '5000'))

    # Email (SMTP) – used by contact form and EmailService
    SMTP_SERVER: str = os.getenv('SMTP_SERVER', '')
    SMTP_PORT: str = os.getenv('SMTP_PORT', '587')
    SMTP_USERNAME: str = os.getenv('SMTP_USERNAME', '')
    SMTP_PASSWORD: str = os.getenv('SMTP_PASSWORD', '')
    RECIPIENT_EMAIL: str = os.getenv('RECIPIENT_EMAIL', '')

    # Rate Limiting Configuration
    RATE_LIMIT_DEFAULTS: str = os.getenv('RATE_LIMIT_DEFAULTS', '5 per minute')
    RATE_LIMIT_STORAGE_URI: str = os.getenv('RATE_LIMIT_STORAGE_URI', 'memory://')

    @classmethod
    def validate_email_config(cls) -> bool:
        """Return True if email is configured enough to send contact form messages."""
        return bool(
            cls.SMTP_SERVER and cls.SMTP_USERNAME and cls.SMTP_PASSWORD and cls.RECIPIENT_EMAIL
        )