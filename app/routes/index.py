"""
Index Routes

Home page and health check endpoints for the portfolio website.
"""

from flask import Blueprint, jsonify

# Create a Blueprint for the index routes
index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    """Root endpoint to welcome the user to the portfolio website."""
    return jsonify({'message': 'Welcome to the Portfolio website'}), 200


@index_bp.route('/health')
def health():
    """Health check endpoint to verify the application is running."""
    return jsonify({
        'message': 'Health check successful',
        'status': 'healthy'
    }), 200