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
    file.save(f"uploads/{uTimeDate+file.filename}")
    fileServerPath = 'uploads/'+uTimeDate+file.filename
    fileName = main_my(fileServerPath)
    # splitFileN = fileName.split(",")
    hostName = request.headers.get('Host')
    # breakpoint()
    return jsonify({"success": True, "file": hostName+'/'+fileName[0],"image":hostName+'/'+fileName[1]})
