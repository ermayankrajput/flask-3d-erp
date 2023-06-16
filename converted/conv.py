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
    file = request.files["u_file"]
    # uniqueFileName = str(datetime.now().timestamp()).replace(".","")
    file.save(f"uploads/{file.filename}")
    fileServerPath = 'uploads/'+file.filename
    fileName = main_my(fileServerPath)
    hostName = request.headers.get('Host')
    return jsonify({"success": True, "file": hostName+'/'+fileName})