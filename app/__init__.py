from flask import Flask
from .extensions import db
from .routes.main import main_blueprint

def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Extensions
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(main_blueprint)

    return app