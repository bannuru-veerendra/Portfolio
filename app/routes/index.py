"""
Index Routes

Home page and health check endpoints for the portfolio website.
"""

from flask import Blueprint, jsonify, render_template

# Create a Blueprint for the index routes
index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    """Root endpoint to render the portfolio homepage."""
    return render_template('index.html')


@index_bp.route('/health')
def health():
    """Health check endpoint to verify the application is running."""
    return jsonify({
        'message': 'Health check successful',
        'status': 'healthy'
    }), 200