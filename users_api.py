from datetime import datetime
from flask import abort, jsonify, request,Blueprint
from database.database_models import User,Role,db
from sqlalchemy import func
# from flask_security import roles_accepted

user_api_blueprint = Blueprint('user_api_blueprint', __name__)



@user_api_blueprint.route('/signup/<int:role_id>/', methods = ['POST'])
def sign_up(role_id):
    user = User.query.filter_by(email=request.json['email']).first()
    role = Role.query.get(role_id)
    if user:
        msg="User already exist"
        return msg 
    user = User(email='this@gmaigh5.com', status=1,first_name= 'lol',last_name= 'ji',email_confirmed_at= str(datetime.now()), password='password',age = 34,role_id=role.id)
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