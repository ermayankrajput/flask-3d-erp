from datetime import datetime

def unique_fileName(fileName = ''):
    return str(datetime.now().timestamp()).replace(".","") + fileName