from functools import wraps
from flask import Flask, abort,jsonify, request ,Blueprint, send_from_directory
# from flask_login import LoginManager, login_manager, login_user
# from flask_sqlalchemy import SQLAlchemy
import os
# from flask_migrate import Migrate
# from multiprocessing import Process
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
# import jwt
# from flask_seeder import FlaskSeeder
# import multiprocessing
# from streamlit import caching

from sqlalchemy import text
import trimesh
from flask_cors import CORS
# from flask_seeder import FlaskSeeder

# from OpenSSL import SSL
# context = SSL.Context(SSL.TLSv1_2_METHOD)
# context.use_privatekey_file('key.pem')
# context.use_certificate_file('cert.pem')

# from mesh_converter import meshRun

# app = Flask(__name__, static_folder='transported')
app = Flask(__name__, static_folder='downloads')
CORS(app)
app.url_map.strict_slashes = False
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/db3erp"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '128566299290685828278054891499021371965'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# seeder = FlaskSeeder()
# seeder.init_app(app, db)
# with app.app_context():
#     with db.engine.connect() as conn:
#         conn.execute(text("drop table alembic_version"))

# from database.database_models import User
# decorator factory which invoks update_wrapper() method and passes decorated function as an argument

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    r.headers['Access-Control-Allow-Headers'] = 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token, x-access-token'
    r.headers['Access-Control-Allow-Origin'] = '*'
    r.headers['Access-Control-Allow-Methods'] = "GET, POST, PUT, DELETE, OPTIONS,PATCH"
    return r

# if __name__ == '__main__':
    # app.run(ssl_context=context)

# from converted.conv import conv_blueprint
# app.register_blueprint(conv_blueprint)

from quote.quote_api import quote_api_blueprint
app.register_blueprint(quote_api_blueprint)

from users.users_api import user_api_blueprint
app.register_blueprint(user_api_blueprint)

from exchange.exchange_api import exchange_api_blueprint
app.register_blueprint(exchange_api_blueprint)

@app.route('/testm',methods=['GET', 'POST'])
def test():
    file = request.files["file"]
    uniqueFileName = str(datetime.now().timestamp()).replace(".","")
    uTimeDate = str(uniqueFileName)
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    file.save(f"uploads/{uTimeDate+file.filename}")
    fileServerPath = 'uploads/'+uTimeDate+file.filename
    hostName = request.headers.get('Host')

@app.route('/')
def index():
    return jsonify({"message": "Welcome to my quote data"})

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def responseTransportedFile(filename):
    send_from_directory(app.static_folder, filename)


@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def responseTransportedImgFile(filename):
    send_from_directory(app.static_folder, filename)

@app.route('/temp-uploads/<path:filename>', methods=['GET', 'POST'])
def responseTempImgFile(filename):
    send_from_directory(app.static_folder, filename)
