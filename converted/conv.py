import multiprocessing
from flask import Blueprint
from flask import Flask, abort, jsonify, request
import os
import sys
from helpers.unique_fileName import allow_file, allowed_file, unique_fileName
from helpers.uploaders import uploadToS3
from transfers.transfer_function import cadex_Converter
sys.path.append("conversion/transfer")

conv_blueprint = Blueprint('conv_blueprint', __name__)
@conv_blueprint.route("/convert",methods = ['POST'])
def conversion():
    file = request.files["file"]
    if file and allowed_file(file.filename):
        uniqueFileName = unique_fileName(file.filename)
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
        file.save(f"uploads/{uniqueFileName}")
        fileServerPath = 'uploads/'+uniqueFileName
   # array of ext.....
    # listExt = ["stp","stl","STL","step","catpart","igs","prt","sat","sldprt","x_t","STP","STEP","CATPART","IGS","PRT","SAT","SLDPRT","X_T"]
    # check file extension condition
    fileNameSplit = file.filename.split(".")
    # ext = fileNameSplit[len(fileNameSplit)-1]
    # if not ext in listExt:
    #     return jsonify({"success": False, "message": "Invalid file type"}) 
    # if ext not in ["stl", "STL"]:
    if not allow_file(file.filename):
        cadex_Converter(fileServerPath, uniqueFileName)
    # transported_file = fileServerPath if ext in ["stl", "STL"] else str(fileServerPath) + '.stl'
    transported_file = fileServerPath if allow_file(file.filename)else str(fileServerPath) + '.stl'
    uploadProcess = multiprocessing.Process(target=uploadToS3, args=(fileServerPath, ))
    uploadProcess.start()
    return jsonify({"success": True, "file_name":file.filename,"uploded_file": fileServerPath, "transported_file": transported_file,"image_file": fileServerPath + '.png'})
