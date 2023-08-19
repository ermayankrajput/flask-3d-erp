from flask import Blueprint
from database.database_models import Role,db


# user_role_blueprint = Blueprint('user_role_blueprint', __name__)

def create_roles():
    roles = ['admin', 'engineer', 'user'] 

    for role_name in roles:
        role = Role(name=role_name)
        db.session.add(role)
    db.session.commit()

# create_roles()

