from flask import Blueprint
from .player_routes import user_bp

def register_blueprints(app):
    app.register_blueprint(user_bp, url_prefix='/api')   # Prefixes all routes with /api
    app.register_blueprint(product_bp, url_prefix='/api') # Prefixes all routes with /api
