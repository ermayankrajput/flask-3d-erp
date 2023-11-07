from datetime import datetime, timedelta
from flask import abort, jsonify, make_response, request,Blueprint
# from flask_jwt_extended import current_user
# from flask_security import roles_accepted
# from flask_login import LoginManager, login_required, logout_user
import jwt
# from  werkzeug.security import generate_password_hash, check_password_hash
from users.auth_middleware import generate_token, token_required, roles_required, ADMIN_ROLE, USER_ROLE, is_current_user
from database.database_models import Quote, QuoteInfo, UnitQuote, User,Role,db
from app import app 
from sqlalchemy import func
# from flask_security import roles_accepted
# from flask_jwt_extended import create_access_token, current_user
import bcrypt
from alembic import op
import sqlalchemy

from alembic.migration import MigrationContext
from alembic.operations import Operations

user_api_blueprint = Blueprint('user_api_blueprint', __name__)

def generateHashedPassword(password):
    salt = b'$2b$12$zMaf1M1t4VkonfP/AW8maO'
    return bcrypt.hashpw(password.encode(), salt)

@user_api_blueprint.route('/signup/', methods = ['POST'])
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



@user_api_blueprint.route('/register-role/', methods = ['GET'])
def register_role():
    # role = Role(id=1, name = 'admin', status = 1)
    # db.session.add(role)
    # role = Role(id=2, name = 'user', status = 1)
    # db.session.add(role)
    # db.session.commit()
    roles = Role.query.all()
    result = [role.serialize() for role in roles]
    # return jsonify(role.serialize())
    return jsonify(result)



@user_api_blueprint.route('/user/<int:user_id>/', methods = ['GET'])
@roles_required(ADMIN_ROLE, USER_ROLE)
def getUser(user_id):
    user = User.query.get(user_id)
    if user:
        msg="Invalid user Id"
        return msg
    return jsonify(user.serialize())


@user_api_blueprint.route('/user-role/<int:role_id>/', methods = ['GET'])
@roles_required(ADMIN_ROLE, USER_ROLE)
def getRole(role_id):
    user = Role.query.get(role_id)
    if user is None:
        abort(404)
    return jsonify(user.serialize())

 

@user_api_blueprint.route('/user/', methods = ['PATCH'])
@roles_required(ADMIN_ROLE, USER_ROLE)
def updateUser():
    user = User.query.get(request.json["id"])
    if user is None:
        abort(404)
    else:
        db.session.query(User).filter_by(id=user.id).update(request.json)
        db.session.commit()
        return jsonify(user.serialize())
    

@user_api_blueprint.route("/user/", methods = ["DELETE"])
@roles_required(ADMIN_ROLE, USER_ROLE)
def deleteUser():
    if User.query.filter_by(id=request.json["id"]).delete():
        db.session.commit()
        return jsonify({"success":True, "response": "User deleted","id":request.json["id"]})
    return jsonify({"success":False, "response": "User ID: "+ str(request.json["id"]) +" Not Found"})


# route for logging user in


@user_api_blueprint.route('/login/', methods =['POST'])
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
            {'WWW-Authenticate' : 'Basic realm ="Wrong username or Password !!"'}
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
        {'WWW-Authenticate' : 'Basic realm ="Wrong username or Password !!"'}
    )


@user_api_blueprint.route("/get/user/", methods=["GET"])
@token_required
def get_current_user(current_user):
    return jsonify({"success":"true","message":"The messange from server","current_user":current_user.serialize()})

@user_api_blueprint.route("/drop-table", methods=["GET"])
def drop_table_fun():
    # Connection
    connection_string = 'postgresql://postgres:password@demo-postgres.ctaazxcq9s9r.us-east-1.rds.amazonaws.com:5432'
    engine = sqlalchemy.create_engine(connection_string)

    # Create migration context
    mc = MigrationContext.configure(engine.connect())

    # Creation operations object
    ops = Operations(mc)
    
    if ops.drop_table('alembic_version'):
        return jsonify({"success":"true","message":"drop table from server"})
    # return jsonify({"success":"true","message":"drop table from server"})



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


@user_api_blueprint.route('/access/', methods=["GET"])
@roles_required(ADMIN_ROLE, USER_ROLE)
def teachers(current_user):
    return jsonify(current_user.serialize())


@user_api_blueprint.route('/share/<uuid>/<email>/', methods = ["POST"] )
@is_current_user
def shared_user(current_user, email, uuid):
    token = ''
    if not current_user:
        if not email:
            return False
        user = User.query.filter_by(email = email).first()
        if not user:
            user = User(email=email, status=1,email_confirmed_at= str(datetime.now()), role_id=2)
            db.session.add(user)
            db.session.commit()
        current_user = user
        token = generate_token(current_user)
        if not uuid:
            return False
        old_quote = Quote.query.filter_by(uuid = uuid).first()
        quote = Quote.query.filter_by(parent_id = old_quote.id, user_id = current_user.id).first()
        if quote:
            return jsonify({'token' : token, 'quote': quote.serialize()})
        quote = Quote(quote_date = str(datetime.now()), validity = None, shipping_cost = None, grand_total = None, attachments = old_quote.attachments, user_id = current_user.id, parent_id = old_quote.id,)
        db.session.add(quote)
        db.session.commit()
        old_quoteinfos = QuoteInfo.query.filter_by(quote_id = old_quote.id)
        for quoteinfo in old_quoteinfos:
            quoteinfo = QuoteInfo(uploded_file = quoteinfo.uploded_file ,file_name = quoteinfo.file_name,transported_file =quoteinfo.transported_file ,material_search = quoteinfo.material_search,technique = quoteinfo.technique,finishing = quoteinfo.finishing,x_size = quoteinfo.x_size,y_size= quoteinfo.y_size,z_size = quoteinfo.z_size,quote_id = quote.id,image_file=quoteinfo.image_file)
            db.session.add(quoteinfo)
            db.session.commit()
            unitquote = UnitQuote(unit_price = None,quantity = None,lead_time=None,quote_info_id=quoteinfo.id)
            db.session.add(unitquote)
            db.session.commit()
    return jsonify({'token' : token, 'quote': quote.serialize()})


