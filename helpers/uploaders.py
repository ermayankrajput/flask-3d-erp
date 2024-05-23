from s3_upload import s3_upload
import os

def uploadToS3(filePath):
    # if not filePath.split(".")[-1] in ['stl', "STL"]:
        # s3_upload(filePath, filePath + '.stl')
    s3_upload(filePath + '.jpg', filePath + '.jpg')
    s3_upload(filePath, filePath)
    emptyUploadFolder()
    return


def emptyUploadFolder():
    for f in os.listdir('uploads'):
        os.remove(os.path.join('uploads', f))



def uploadFileToS3(file):
    for i  in range(len(file)):
        s3_upload(file[i],file[i])
    return

# def get_user_role(): 
#     if current_user.is_authenticated:
#         return current_user.role
#     return None