from s3_upload import s3_upload, s3_delete
import os

def uploadToS3(filePath):
    # if not filePath.split(".")[-1] in ['stl', "STL"]:
        # s3_upload(filePath, filePath + '.stl')
    s3_upload(filePath + '.jpg', filePath + '.jpg')
    s3_upload(filePath, filePath)
    # emptyUploadFolder()
    return

def deleteFromS3(filePath):
    s3_delete(filePath)
    return True

def emptyUploadFolder():
    for f in os.listdir('uploads'):
        os.remove(os.path.join('uploads', f))



def uploadFileToS3(file):
    for i  in range(len(file)):
        s3_upload(file[i],file[i])
    # emptyUploadFolder()
    return

# def get_user_role(): 
#     if current_user.is_authenticated:
#         return current_user.role
#     return None