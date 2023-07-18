from flask import Blueprint
from flask import Flask, abort, jsonify, request
# from conversion import*
# from transfer_function import main_my
import os
from datetime import datetime
import sys
from pathlib import Path

sys.path.append("conversion/transfer")
from transfer_function import main_my
import socket
import platform
from s3_upload import s3_upload

conv_blueprint = Blueprint('conv_blueprint', __name__)




@conv_blueprint.route("/convert",methods = ['POST'])
def conversion():
    file = request.files["file"]
    # breakpoint()
   # array of ext.....
    listExt = ["stp","stl","STL","step","catpart","igs","prt","sat","sldprt","x_t","STP","STEP","CATPART","IGS","PRT","SAT","SLDPRT","X_T"]
    # check file extension condition
    fileNameSplit = file.filename.split(".")
    ext = fileNameSplit[len(fileNameSplit)-1]
    # breakpoint()
    if not ext in listExt:
        return jsonify({"success": False, "message": "Invalid file type"}) 

    uniqueFileName = str(datetime.now().timestamp()).replace(".","")
    uTimeDate = str(uniqueFileName)
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    newFileName = uTimeDate+file.filename
    file.save(f"uploads/{newFileName}")
    fileServerPath = 'uploads/'+newFileName
    cadexFiles = main_my(fileServerPath, newFileName)
    s3UploadedFile = s3_upload(fileServerPath, newFileName)
    s3ImageFile = s3_upload('uploads/' + newFileName + '.pdf.png', newFileName + '.pdf.png')
    s3TransportedFile = s3_upload('uploads/' + newFileName + '.stl', newFileName + '.stl')
    return jsonify({"success": True,"uploded_file": s3UploadedFile, "transported_file": newFileName + '.stl',"image_file": newFileName + '.pdf.png'})
