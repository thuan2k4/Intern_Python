from flask import Flask
from extensions import db
from auth import auth_bp
from users import users_bp
from dotenv import load_dotenv
from middleware import init_app_jwt

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Tự nạp biến môi trường, mặc định sẽ là tiền tối "FLASK_%"
    # có thể tùy chình tiền tố bằng tham số (prefix="...")
    app.config.from_prefixed_env() 
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(users_bp, url_prefix='/users')
    
    db.init_app(app)
    init_app_jwt(app)
    
    with app.app_context():
        db.create_all()
    
    return app
