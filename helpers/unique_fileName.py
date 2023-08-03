from datetime import datetime

ALLOWED_EXTENSIONS = set(["stp","step","igs","iges","stl","png"])

def allowed_file(filename):
    ext =  '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
    return ext

ALLOW_EXT = set(["stl"])
def allow_file(filename):
    ext =  '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOW_EXT
    return ext

def unique_fileName(fileName = ''):
    return str(datetime.now().timestamp()).replace(".","") + fileName