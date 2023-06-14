from flask import Flask, abort,jsonify, request ,Blueprint
from flask_sqlalchemy import SQLAlchemy
import json
# from streamlit import caching


# import trimesh

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:password@localhost/pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# caching.clear_cache()
from Pets.petApi import petApi_blueprint
app.register_blueprint(petApi_blueprint)
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

    

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)

# from Pets.petApi import *
# from converters.converter import *

# mesh = trimesh.Trimesh(**trimesh.interfaces.gmsh.load_gmsh(file_name = 'images/Convert.stp', gmsh_args = [
#             ("Mesh.Algorithm", 1), #Different algorithm types, check them out
#             ("Mesh.CharacteristicLengthFromCurvature", 50), #Tuning the smoothness, + smothness = + time
#             ("General.NumThreads", 10), #Multithreading capability
#             ("Mesh.MinimumCirclePoints", 32)])) 
# print("Mesh volume: ", mesh.volume)
# print("Mesh Bounding Box volume: ", mesh.bounding_box_oriented.volume)
# print("Mesh Area: ", mesh.area)

    
    ## Export the new mesh in the STL format
# mesh.export('converted_in.STL')


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    # r.headers['Content-Type'] = 'application/json'
    return r

@app.route('/')
def index():
    return jsonify({"message": "Welcome to my pet store"})



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
