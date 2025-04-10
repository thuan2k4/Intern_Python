from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt, current_user, get_jwt_identity
from models import User, TokenBlockedList
from datetime import datetime, timezone

auth_bp = Blueprint('auth', __name__)

@auth_bp.post('/register')
def register_user():
    data = request.get_json()
    user = User.get_user_by_username(data['username'])
    
    if user:
        return jsonify({'message': 'User already exists'}), 400
    
    new_user = User(
        username=data['username'],
        email=data['email'],
    )
    new_user.set_password(password=data['password'])
    new_user.add()
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.post('/login')
def login_user():
    data = request.get_json()
    user = User.get_user_by_username(data['username'])
    
    if user and user.check_password(password=data['password']):
        access_token = create_access_token(identity=user.username)
        refresh_token = create_refresh_token(identity=user.username)
        
        return jsonify(
            {
                'message': 'Logged in successfully', 
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        ), 200

    return jsonify({'message': 'Invalid credentials'}), 400

@auth_bp.get('/whoami')
@jwt_required()
def whoami():
    #claims = get_jwt() #user info (contain role)

    return jsonify({
        'message': 'Who Am I ?',
        'user_details': {
            "username": current_user.username,
            "email": current_user.email
        }
    }), 200
#current_user is loaded @jwt.user_lookup_loader

@auth_bp.get('/refresh')
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify({
        'username': identity,
        'message': 'Token refreshed successfully',
        'access_token': access_token
    }), 200

#revoke token
@auth_bp.get('/logout')
@jwt_required(verify_type=False)
def logout_user():
    jwt = get_jwt()
    jti = jwt['jti']
    token = TokenBlockedList(jti=jti)
    token_type = jwt['type']
    token.add()
    
    return jsonify({
        'message': f'{token_type} token revoked successfully'
    }), 200
