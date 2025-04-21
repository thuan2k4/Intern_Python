from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from models import User
from schemas import UserSchema
from models import TokenBlockedList

users_bp = Blueprint('users', __name__)

@users_bp.get('/all')
@jwt_required() #check token exists
def get_all_users():
    #check if user is staff
    
    check = TokenBlockedList.query.filter_by(jti=get_jwt().get('jti'))
    print(f"check: {check}")
    
    claims = get_jwt()
    if claims['is_staff'] == False:
        return jsonify({
            "message": "You are not authorized to access this resource."
        }), 403
    
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 2, type=int)
    
    #list all users
    users = User.query.paginate(
        page=page,
        per_page=per_page
    )
    
    #Dict -> JSON
    result = UserSchema().dump(users, many=True)
    
    return jsonify({
        "users":result
    }), 200

