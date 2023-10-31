from datetime import datetime, timedelta
from flask import abort, jsonify, make_response, request,Blueprint
# from flask_login import login_user
import jwt
from  werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from database.database_models import User,Role,db
from app import app 
from sqlalchemy import func
from flask_security import roles_accepted
from flask_jwt_extended import create_access_token
import bcrypt


user_api_blueprint = Blueprint('user_api_blueprint', __name__)

def generateHashedPassword(password):
    salt = b'$2b$12$zMaf1M1t4VkonfP/AW8maO'
    return bcrypt.hashpw(password.encode(), salt)

@user_api_blueprint.route('/signup', methods = ['POST'])
def sign_up():
    user = User.query.filter_by(email=request.json['email']).first()
    # role = Role.query.get(role_id)
    if user:
        msg="User already exist"
        return msg 
    
    # Hashing the password
    # breakpoint()
    user = User(email=request.json['email'], status=1, first_name= 'lol',last_name= 'ji',email_confirmed_at= str(datetime.now()), password = generateHashedPassword(request.json['password']).decode(),age = 34,role_id=1)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())



@user_api_blueprint.route('/register-role/', methods = ['POST'])
def register():
    role = Role(name = 'Engineer', status = 1)
    db.session.add(role)
    db.session.commit()
    return jsonify(role.serialize())



@user_api_blueprint.route('/user/<int:user_id>/', methods = ['GET'])
def getUser(user_id):
    user = User.query.get(user_id)
    return jsonify(user.serialize())



@user_api_blueprint.route('/user-role/<int:role_id>/', methods = ['GET'])
def getRole(role_id):
    user = Role.query.get(role_id)
    return jsonify(user.serialize())

 

@user_api_blueprint.route('/user/', methods = ['PATCH'])
def updateQuote():
    user = User.query.get(request.json["id"])
    if user is None:
        abort(404)
    else:
        db.session.query(User).filter_by(id=user.id).update(request.json)
        db.session.commit()
        # breakpoint()
        return jsonify(user.serialize())
    



@user_api_blueprint.route("/user/", methods = ["DELETE"])
def deleteQuote():
    if User.query.filter_by(id=request.json["id"]).delete():
        db.session.commit()
        return jsonify({"success":True, "response": "User deleted","id":request.json["id"]})
    return jsonify({"success":False, "response": "User ID: "+ str(request.json["id"]) +" Not Found"})


# route for logging user in


@user_api_blueprint.route('/login', methods =['POST'])
def login():
    # creates dictionary of form data
    auth = request.json
    
    # breakpoint()
    if not auth or not auth.get('email') or not auth.get('password'):
        
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
    # breakpoint()
    user = User.query.filter_by(email = auth.get('email')).first()
  
    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
    # breakpoint()
    if user.password == generateHashedPassword(auth.get('password')).decode():
        # generates the JWT Token
        
        token = jwt.encode({
            'public_id': user.id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, app.config['SECRET_KEY'], algorithms=["HS256"])
        return jsonify({'success': True,'token' : token})
    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )
