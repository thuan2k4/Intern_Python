from flask import Flask, jsonify
from extensions import db, jwt
from auth import auth_bp
from users import users_bp
from middleware import init_app_jwt, jwt_middleware

def create_app():
    app = Flask(__name__)
    
    app.config.from_prefixed_env()
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(users_bp, url_prefix='/users')
    
    db.init_app(app)
    init_app_jwt(app)
    
    return app
