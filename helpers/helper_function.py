import datetime
import os
from flask import app
import jwt

ALLOWED_EXTENSIONS = set(["stp","step","igs","iges","stl","png"])

def allowed_file(filename):
    ext =  '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
    return ext

ALLOW_EXT = set(["stl"])
def isStl(filename):
    ext =  '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOW_EXT
    return ext

def unique_fileName(fileName = ''):
    return str(datetime.datetime.now().timestamp()).replace(".","") + fileName

def unique_fileName_with_path(path):
    path = path.replace(os.sep, '/')
    ext =  '.' in path and path.rsplit('.',1)[1].lower()
    return path + str(datetime.datetime.now().timestamp()) + '.' + ext

def generate_json_data(file_data_list):
    json_data = {
        "file": [
            {
                "file": item["file"],
                "filename":item["filename"],
                "date": item["date"]
            }
            for item in file_data_list
        ]
    }
    return json_data


def generate_json(file_data):
    json1_data = {
        "file": [
            {
                "filename": item["filename"],
                "transported": item["transported"],
                "image": item["image"]
            }
            for item in file_data
        ]
    }
    return json1_data


def filter_files_by_extension(file):
    # matching_extensions = {"stp", "step", "igs", "iges", "stl"}
    matching_3d_extensions = {"stl", "STL"}
    # matching_3d_extensions = {"stp", "stl", "STL", "step", "catpart", "igs", "iges", "prt", "sat", "sldprt", "x_t", "STP", "STEP", "CATPART", "IGS", "IGES", "PRT", "SAT", "SLDPRT", "X_T"}
    zip_extension = {"zip", "ZIP"}
    matching3d_files = []
    non3d_matching_files = []
    zip_files = []
    file_extension = os.path.splitext(file)[1][1:].lower()
    if file_extension in matching_3d_extensions:
        matching3d_files.append(file)
    elif file_extension in zip_extension:
        zip_files.append(file)
    else:
        non3d_matching_files.append(file)
        
    return matching3d_files, non3d_matching_files, zip_files

ALLOW_EXTENSIONS = {'zip'}
def iszip(filename):
    ext =  '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOW_EXTENSIONS
    return ext


# def njjf():
#     if not @roles_required(ADMIN_ROLE, USER_ROLE)