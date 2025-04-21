from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt, current_user, decode_token
from models import User, TokenBlockedList, TokenPair

auth_bp = Blueprint('auth', __name__)

def blockToken(jti):
    token = TokenBlockedList(jti=jti)
    token.add()

def addCurrentTokenintoDB(access_token, refresh_token):
    tokenPair = TokenPair(access_jti=decode_token(access_token)['jti'], refresh_jti= decode_token(refresh_token)['jti'])
    tokenPair.add()

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
        
        addCurrentTokenintoDB(access_token, refresh_token)
        
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


@auth_bp.get('/refresh')
@jwt_required(refresh=True)
def refresh():
    jwt = get_jwt()
    jti = jwt['jti']
    identity = jwt['sub']
    
    findTokeninDB = TokenPair.query.filter_by(refresh_jti=jti).first()
    if findTokeninDB:
        blockToken(findTokeninDB.access_jti)
    
    blockToken(jti)
    
    access_token = create_access_token(identity=identity)
    refresh_token = create_refresh_token(identity=identity)
    
    addCurrentTokenintoDB(access_token, refresh_token)
    
    return jsonify({
        'username': identity,
        'message': 'Token refreshed successfully',
        'access_token': access_token,
        'refresh_token': refresh_token
    }), 200

#revoke token
@auth_bp.get('/logout')
@jwt_required(verify_type=False)
def logout_user():
    jwt = get_jwt()
    jti = jwt['jti']
    token_type = jwt['type']
    
    blockToken(jti)
    
    return jsonify({
        'message': f'{token_type} token revoked successfully'
    }), 200
