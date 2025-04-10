from flask import Flask, jsonify
from extensions import db, jwt
from auth import auth_bp
from users import users_bp
from models import User, TokenBlockedList

def create_app():
    app = Flask(__name__)
    
    app.config.from_prefixed_env()
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(users_bp, url_prefix='/users')
    
    db.init_app(app)
    jwt.init_app(app)
    
    #load user (use for method current_user)
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data['sub'] #query username in jwt
        return User.query.filter_by(username=identity).one_or_none() #just 1 query
    
    #additional claims loader
    @jwt.additional_claims_loader
    def add_claims_to_access_token(identity):
        if identity == 'Carol':
            return {"is_staff": True}
        return {"is_staff": False}
    
    # jwt error handler
    
    #Token hết hạn
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            "message": "The token has expired.",
            "error": "token_expired"
        }), 401
    
    #Token không hợp lệ
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            "message": "Signature verification failed.",
            "error": "invalid_token"
        }), 401
    
    #Không có token
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({
            "message": "Request does not contain an access token.",
            "error": "authorization_required"
        }), 401
    
    #check if token is revoked
    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        token = db.session.query(TokenBlockedList).filter(TokenBlockedList.jti == jti).scalar()
        return token is not None
    
    return app
