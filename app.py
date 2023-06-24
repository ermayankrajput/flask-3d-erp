from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
import os
# from flask_migrate import Migrate
# from multiprocessing import Process

# from datetime import datetime
# import multiprocessing
# from streamlit import caching

# import trimesh

# from mesh_converter import meshRun

# app = Flask(__name__, static_folder='transported')
app = Flask(__name__, static_folder='uploads')
# print(app.static_folder)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:password@localhost/three_erp'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# @app.after_request
# def add_header(r):
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     r.headers['Access-Control-Allow-Origin'] = '*'
#     return r
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# caching.clear_cache()
# from Pets.petApi import petApi_blueprint
# app.register_blueprint(petApi_blueprint)

# from converted.conv import conv_blueprint
# app.register_blueprint(conv_blueprint)

# from database.database_models import database_models_blueprint
# app.register_blueprint(database_models_blueprint)

# from quote.quote_api import quote_api_blueprint
# app.register_blueprint(quote_api_blueprint)

# class quote(db.model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.date,nullable = False)
#     validity = db.Column(db.Integer(),nullable = False)
#     shipping_cost = db.Column(db.Integer(),nullable = False)
#     grand_total = db.Column(db.Integer(),nullable = False)





# from converters.converter import converter_blueprint
# app.register_blueprint(converter_blueprint)
# db = SQLAlchemy(app)
# print(__name__)
# class Pet(db.Model):
#     __tablename__ = 'pets'
#     id = db.Column(db.Integer, primary_key = True)
#     pet_name = db. Column(db.String(100), nullable = False)
#     pet_type = db.Column(db.String(100), nullable = False)
#     pet_age = db.Column(db.Integer(), nullable = False)
#     pet_description = db.Column(db.String(100), nullable = False)


#     def __repr__(self):
#         return "<Pet %r>" % self.pet_name
    
# with app.app_context():
#     db.create_all()


# @app.route('/')
# def index():
#     return jsonify({"message": "Welcome to my pet store"})
# class GracefulKiller:
#   kill_now = False
#   def __init__(self):
#     signal.signal(signal.SIGINT, self.exit_gracefully)
#     signal.signal(signal.SIGTERM, self.exit_gracefully)

#   def exit_gracefully(self, *args):
#     self.kill_now = True

    

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)
    # db.create_all()
    # app.run(debug=True)
    # killer = GracefulKiller()
    # while not killer.kill_now:
    #     time.sleep(1)
@app.route('/')
def index():
    return jsonify({"message": "Welcome to my quote data"})

# __init__.py

# from Pets.petApi import *
# from converters.converter import *
# ret = {'foo': False, "converted_file": ""}

# @app.route('/testm',methods=['GET', 'POST'])
# def test():
#     file = request.files["file"]
#     uniqueFileName = str(datetime.now().timestamp()).replace(".","")
#     uTimeDate = str(uniqueFileName)
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#     file.save(f"uploads/{uTimeDate+file.filename}")
#     fileServerPath = 'uploads/'+uTimeDate+file.filename
#     hostName = request.headers.get('Host')
    # breakpoint()


    # fileName = main_my(fileServerPath)
    # procs = []
    # proc = Process(target=meshRun)  # instantiating without any argument
    # procs.append(proc)
    # proc.start()
    # return "working on it"
    # queue = multiprocessing.Queue()
    # queue.put(ret)
    # p = multiprocessing.Process(target=meshRun, args=(queue,fileServerPath,))
    # p.start()
    # p.join()
    # queueInfo  = queue.get()   
    # return jsonify({"success": True, "file": queueInfo['converted_file']})

# def meshRun(queue,fileServerPath):
#     fileNameSplit = fileServerPath.split("/")    
#     FileMainName = fileNameSplit[len(fileNameSplit)-1]
#     splitFile = FileMainName.split(".")
#     splitFileFirstName = splitFile[len(splitFile)-2]
#     ret = queue.get()
#     mesh = trimesh.Trimesh(**trimesh.interfaces.gmsh.load_gmsh(fileServerPath, gmsh_args = [
#                 ("Mesh.Algorithm", 2), #Different algorithm types, check them out
#                 ("Mesh.CharacteristicLengthFromCurvature", 50), #Tuning the smoothness, + smothness = + time
#                 ("General.NumThreads", 10), #Multithreading capability
#                 ("Mesh.MinimumCirclePoints", 32)])) 
#     print("Mesh volume: ", mesh.volume)
#     # print("Mesh Bounding Box volume: ", mesh.bounding_box_oriented.volume)
#     print("Mesh Area: ", mesh.area)

#     if not os.path.exists('uploads/transported'):
#         os.makedirs('uploads/transported')
#     # Export the new mesh in the STL format
#     mesh.export('uploads/transported/'+splitFileFirstName+'.stl')
#     ret['foo'] = True
#     ret['converted_file'] = 'uploads/transported/'+splitFileFirstName+'.stl'
#     queue.put(ret)

# @app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
# def responseTransportedFile(filename):
#     send_from_directory(app.static_folder, filename)


# @app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
# def responseTransportedImgFile(filename):
#     send_from_directory(app.static_folder, filename)


# @app.route("/pets/<int:pet_id>", methods = ["DELETE"])
# def delete_pet(pet_id):
#     pet = Pet.query.filter_by(id=pet_id)

#     if pet is None:
#         abort(404)
#     else:
#         pet.delete()
#         db.session.commit()
#         return jsonify({"success": True, "response": "Pet deleted"})

# @app.route("/pets/<int:pet_id>", methods = ["PATCH"])
# def update_pet(pet_id):
#     pet = Pet.query.get(pet_id)
#     if pet is None:
#         abort(404)
#     else:
#         # pet.pet_age = request.json['pet_age']
#         # pet.pet_description = request.json.get('pet_description') or pet.pet_description
#         # db.session.add(pet)
#         db.session.query(Pet).filter_by(id=pet_id).update(request.json)
#         db.session.commit()
#         return jsonify({"success": True, "response": "Pet Details updated"})



# @app.route('/pets', methods = ['GET'])
# def getpets():
#      all_pets = []
#      pets = Pet.query.all()
#      for pet in pets:
#           results = {
#                     "pet_id":pet.id,
#                     "pet_name":pet.pet_name,
#                     "pet_age":pet.pet_age,
#                     "pet_type":pet.pet_type,
#                     "pet_description":pet.pet_description, }
#           all_pets.append(results)

#      return jsonify(
#             {
#                 "success": True,
#                 "pets": all_pets,
#                 "total_pets": len(pets),
#             }
#         )

# @app.route('/pets', methods = ['POST'])
# def create_pet():
#     pet_data = request.json

#     pet_name = pet_data['pet_name']
#     pet_type = pet_data['pet_type']
#     pet_age = pet_data['pet_age']
#     pet_description = pet_data['pet_description']

#     pet = Pet(pet_name =pet_name , pet_type = pet_type, pet_age = pet_age, pet_description =pet_description )
#     db.session.add(pet)
#     db.session.commit()
    

#     return jsonify({"success": True,"response":"Pet added"})

