from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token
from models import User

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
