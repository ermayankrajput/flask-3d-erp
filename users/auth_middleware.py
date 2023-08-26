from functools import wraps
from flask import jsonify, request
from app import app
import jwt
from database.database_models import Role, User
USER_ROLE = 'User'
ADMIN_ROLE = 'Admin'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
        # breakpoint()
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id = data['public_id']).first()
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
    return decorated

def roles_required(*accepted_roles):
    def wrapper(view_function):

        @wraps(view_function)    # Tells debuggers that is is a function wrapper
        def decorator(*args, **kwargs):
            token = None
            
            # jwt is passed in the request header
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
            # return 401 if token is not passed
            if not token:
                return jsonify({'message' : 'Token is missing !!'}), 401
            # breakpoint()
            try:
                # decoding the payload to fetch the stored details
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                current_user = User.query.filter_by(id = data['public_id']).first()
            except:
                return jsonify({
                    'message' : 'Token is invalid !!'
                }), 401
            # returns the current logged in users context to the routes
            # return  f(current_user, *args, **kwargs)
            # breakpoint()
            role = Role.query.filter_by(id=current_user.role_id).first()
            if role.name not in accepted_roles:
                return jsonify({
                    'message' : 'Not Allowed to perform this action !!'
                }), 401

            # It's OK to call the view
            return view_function(current_user, *args, **kwargs)

        return decorator

    return wrapper