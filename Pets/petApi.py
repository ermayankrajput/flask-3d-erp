from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, abort, jsonify, request
# from converters.converter import converter
from datetime import datetime
import json
from app import app
db = SQLAlchemy(app)
import trimesh
# import signal
# import time


petApi_blueprint = Blueprint('petApi_blueprint', __name__)

class Pet(db.Model):
    # kill_now = False
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key = True)
    pet_name = db. Column(db.String(100), nullable = False)
    pet_type = db.Column(db.String(100), nullable = False)
    pet_age = db.Column(db.Integer(), nullable = False)
    pet_description = db.Column(db.String(100), nullable = False)
    user_file = db.Column(db.Text(), nullable = False)
    
    # def __init__(self):
    #     signal.signal(signal.SIGINT, self.exit_gracefully)
    #     signal.signal(signal.SIGTERM, self.exit_gracefully)

    # def exit_gracefully(self, *args):
    #     self.kill_now = True

    
    def __repr__(self):
        return "<Pet %r>" % self.pet_name
    
with app.app_context():
    db.create_all()



@petApi_blueprint.route("/petst", methods = ["GET"])
def got():
    return jsonify({"success": True, "response": "Pet deleted"})


# @petApi_blueprint.route('/testm')
# def test():
#     mesh = trimesh.Trimesh(**trimesh.interfaces.gmsh.load_gmsh(file_name = 'abc.stp', gmsh_args = [
#                 ("Mesh.Algorithm", 1), #Different algorithm types, check them out
#                 ("Mesh.CharacteristicLengthFromCurvature", 50), #Tuning the smoothness, + smothness = + time
#                 ("General.NumThreads", 10), #Multithreading capability
#                 ("Mesh.MinimumCirclePoints", 32)])) 
#     print("Mesh volume: ", mesh.volume)
#     print("Mesh Bounding Box volume: ", mesh.bounding_box_oriented.volume)
#     print("Mesh Area: ", mesh.area)

#     # Export the new mesh in the STL format
#     mesh.export('converted_in.stl')


@petApi_blueprint.route("/pets/<int:pet_id>", methods = ["DELETE"])
def delete_pet(pet_id):
    pet = Pet.query.filter_by(id=pet_id)

    if pet is None:
        abort(404)
    else:
        pet.delete()
        db.session.commit()
        return jsonify({"success": True, "response": "Pet deleted"})

@petApi_blueprint.route("/pets/<int:pet_id>", methods = ["PATCH"])
def update_pet(pet_id):
    pet = Pet.query.get(pet_id)
    if pet is None:
        abort(404)
    else:
        # pet.pet_age = request.json['pet_age']
        # pet.pet_description = request.json.get('pet_description') or pet.pet_description
        # db.session.add(pet)
        db.session.query(Pet).filter_by(id=pet_id).update(request.json)
        db.session.commit()
        return jsonify({"success": True, "response": "Pet Details updated"})



@petApi_blueprint.route('/pets_get', methods = ['GET'])
def getpets():
     all_pets = []
     pets = Pet.query.all()
     for pet in pets:
          results = {
                    "pet_id":pet.id,
                    "pet_name":pet.pet_name,
                    "pet_age":pet.pet_age,
                    "pet_type":pet.pet_type,
                    "pet_description":pet.pet_description, }
          all_pets.append(results)

     return jsonify(
            {
                "success": True,
                "pets": all_pets,
                "total_pets": len(pets),
            }
        )

@petApi_blueprint.route('/test', methods = ['POST'])
def create_pet():
    # return request.files["user_file"].filename
    # response = requests.post(SERVER_URL, headers={}, data={}, files={"file": open(file_path, 'rb')}, timeout=200)
    # print(request.files["user_file"].filename)
    # breakpoint()
    # return request.data
    file = request.files["u_file"]
    print(file)
    uniqueFileName = str(datetime.now().timestamp()).replace(".","")
    fileNameSplit = file.filename.split(".")
    ext = fileNameSplit[len(fileNameSplit)-1]
    file.save(f"uploads/{uniqueFileName}.{ext}")
    pet_data = request.form
    pet_name = pet_data['pet_name']
    pet_type = pet_data['pet_type']
    pet_age = pet_data['pet_age']
    pet_description = pet_data['pet_description']
    user_file = f"uploads/{uniqueFileName}.{ext}"+file.filename
    pet = Pet(pet_name =pet_name , pet_type = pet_type, pet_age = pet_age, pet_description =pet_description, user_file = user_file)
    # pet = Pet( user_file = user_file)
    db.session.add(pet)
    db.session.commit()
    # breakpoint()
    return jsonify({"success": True,"response":"Pet added"})




# @petApi_blueprint.route('/converted', methods = ['GET'])
# def create_pet():
#     return "this is new"