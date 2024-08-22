# This file can be empty, but it allows the `app` directory to be recognized as a package.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object('flaskr.config.Config')

    # Enable Cross-Origin Resource Sharing
    CORS(app)

    # Initialize SQLAlchemy and Flask-Migrate with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    with app.app_context():
        from . import models, routes
        app.register_blueprint(routes.bp)

    return app

