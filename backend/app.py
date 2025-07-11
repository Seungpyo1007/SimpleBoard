from flask import Flask
from .config import Config
from .models import db
from .routes import main_bp
# If you plan to use Flask-Migrate for database migrations:
# from flask_migrate import Migrate

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    # If using Flask-Migrate:
    # migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(main_bp)

    # Create database tables if they don't exist
    # This is suitable for development but might need a proper migration strategy for production
    with app.app_context():
        db.create_all() # This will create tables based on models.py

    return app

# The following is useful if you run `python backend/app.py` directly
# However, `flask run` (which uses FLASK_APP) is the more common way.
if __name__ == '__main__':
    app = create_app()
    # The port and host can be configured via FLASK_RUN_PORT and FLASK_RUN_HOST in .env
    # or defaults to 5000 and 127.0.0.1 if not set.
    # app.run(debug=app.config.get('DEBUG', True)) # FLASK_DEBUG is preferred
    app.run()
