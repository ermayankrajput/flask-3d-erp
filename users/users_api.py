from datetime import datetime, timedelta
from flask import abort, jsonify, make_response, request,Blueprint
# from flask_jwt_extended import current_user
# from flask_security import roles_accepted
# from flask_login import LoginManager, login_required, logout_user
import jwt
# from  werkzeug.security import generate_password_hash, check_password_hash
from users.auth_middleware import token_required, roles_required, ADMIN_ROLE, USER_ROLE
from database.database_models import User,Role,db
from app import app 
from sqlalchemy import func
# from flask_security import roles_accepted
# from flask_jwt_extended import create_access_token, current_user
import bcrypt
user_api_blueprint = Blueprint('user_api_blueprint', __name__)

def generateHashedPassword(password):
    salt = b'$2b$12$zMaf1M1t4VkonfP/AW8maO'
    return bcrypt.hashpw(password.encode(), salt)

@user_api_blueprint.route('/signup', methods = ['POST'])
def sign_up():
    user = User.query.filter_by(email=request.json['email']).first()
    if user:
        msg="User already exist"
        return msg 
    
    # Hashing the password
    user = User(email=request.json['email'], status=1, first_name= request.json['first_name'],last_name=request.json['last_name'],email_confirmed_at= str(datetime.now()), password = generateHashedPassword(request.json['password']).decode(),age = request.json['age'],role_id=request.json['role_id'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())



# @user_api_blueprint.route('/register-role/', methods = ['POST'])
# def register():
#     role = Role(name = 'Engineer', status = 1)
#     db.session.add(role)
#     db.session.commit()
#     return jsonify(role.serialize())



@user_api_blueprint.route('/user/<int:user_id>', methods = ['GET'])
def getUser(user_id):
    user = User.query.get(user_id)
    if user:
        msg="Invalid user Id"
        return msg
    return jsonify(user.serialize())


@user_api_blueprint.route('/user-role/<int:role_id>', methods = ['GET'])
def getRole(role_id):
    user = Role.query.get(role_id)
    if user is None:
        abort(404)
    return jsonify(user.serialize())

 

@user_api_blueprint.route('/user', methods = ['PATCH'])
def updateUser():
    user = User.query.get(request.json["id"])
    if user is None:
        abort(404)
    else:
        db.session.query(User).filter_by(id=user.id).update(request.json)
        db.session.commit()
        return jsonify(user.serialize())
    

@user_api_blueprint.route("/user", methods = ["DELETE"])
def deleteUser():
    if User.query.filter_by(id=request.json["id"]).delete():
        db.session.commit()
        return jsonify({"success":True, "response": "User deleted","id":request.json["id"]})
    return jsonify({"success":False, "response": "User ID: "+ str(request.json["id"]) +" Not Found"})


# route for logging user in


@user_api_blueprint.route('/login', methods =['POST'])
def login():
    # creates dictionary of form data
    auth = request.json
    
    if not auth or not auth.get('email') or not auth.get('password'):
        
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
    
    user = User.query.filter_by(email = auth.get('email')).first()
  
    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
    
    if user.password == generateHashedPassword(auth.get('password')).decode():
        # generates the JWT Token
       
        token = jwt.encode({
            'public_id': user.id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, app.config['SECRET_KEY'])
        return jsonify({'success': True,'token' : token})
    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )


@user_api_blueprint.route("/get/user", methods=["GET"])
@token_required
def get_current_user(current_user):
    return jsonify(current_user.serialize())


# @LoginManager.user_loader
# def user_loader(user_id):
#     """Given *user_id*, return the associated User object.

#     :param unicode user_id: user_id (email) user to retrieve

#     """
#     return User.query.get(user_id)


# @user_api_blueprint.route("/logout", methods=["GET"])
# @login_required
# def logout():
#     """Logout the current user."""
#     user = current_user
#     user.authenticated = False
#     db.session.add(user)
#     db.session.commit()
#     logout_user()
#     return "Done"


@user_api_blueprint.route('/access', methods=["GET"])
@roles_required(ADMIN_ROLE, USER_ROLE)
def teachers(current_user):
    return jsonify(current_user.serialize())