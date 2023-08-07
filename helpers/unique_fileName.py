from datetime import datetime
import json
import os

from database.database_models import Quote ,db

ALLOWED_EXTENSIONS = set(["stp","step","igs","iges","stl","png"])

def allowed_file(filename):
    ext =  '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
    return ext

ALLOW_EXT = set(["stl"])
def isStl(filename):
    ext =  '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOW_EXT
    return ext

def unique_fileName(fileName = ''):
    return str(datetime.now().timestamp()).replace(".","") + fileName

def generate_json_data(file_data_list):
    json_data = {
        "file": [
            {
                "filename": item["filename"],
                "transported": item["transported"],
                "image": item["image"]
            }
            for item in file_data_list
        ]
    }
    return json_data
import os

def filter_files_by_extension(file):
    matching_extensions = {"stp", "step", "igs", "iges", "stl"}
    matching_files = []
    non_matching_files = []
    file_extension = os.path.splitext(file)[1][1:].lower()
    if file_extension in matching_extensions:
        matching_files.append(file)
    else:
        non_matching_files.append(file)
        
    return matching_files, non_matching_files


# def attachment(file):
#         quote = Quote(quote_date = str(datetime.now()), validity = None, shipping_cost = None, grand_total = None)
#         db.session.add(quote)
#         db.session.commit()