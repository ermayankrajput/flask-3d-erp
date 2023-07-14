import trimesh
import os
from stltojpg import stlToImg
import requests


def meshRun(queue,fileServerPath):
    print(fileServerPath)
    if os.path.isfile(fileServerPath):
        print("file is saved here")
    else:
        print("file not saved here")
    fileNameSplit = fileServerPath.split("/")    
    FileMainName = fileNameSplit[len(fileNameSplit)-1]
    splitFile = FileMainName.split(".")
    splitFileFirstName = splitFile[len(splitFile)-2]
    ret = queue.get()
    # url = "https://wordpress-311437-2997507.cloudwaysapps.com/x-file/abc.stp"
    # r = requests.get(url)
    # file = r.content
    mesh = trimesh.Trimesh(**trimesh.interfaces.gmsh.load_gmsh(fileServerPath, gmsh_args = [
                ("Mesh.Algorithm", 1), #Different algorithm types, check them out
                ("Mesh.CharacteristicLengthFromCurvature", 50), #Tuning the smoothness, + smothness = + time
                ("General.NumThreads", 20), #Multithreading capability
                ("Mesh.MinimumCirclePoints", 32)])) 
    # print("Mesh volume: ", mesh.volume)
    # print("Mesh Bounding Box volume: ", mesh.bounding_box_oriented.volume)
    print("Mesh Area: ")

    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    # Export the new mesh in the STL format
    mesh.export('uploads/'+FileMainName+'.stl')
    # print("MESH CONVERTER", mesh.bounding_box())
    # dimensions = stlToImg('uploads/transported/'+FileMainName+'.stl', 'uploads/images/'+FileMainName+'.stl.png')
    # print("Dimesions stltojpg ", dimensions)
    ret['converted_file'] = 'uploads/'+FileMainName+'.stl'
    # ret['image_file'] = 'uploads/images/'+FileMainName+'.stl.png'
    # ret['x'] = str(dimensions.get("x"))
    # ret['y'] = str(dimensions.get("y"))
    # ret['z'] = str(dimensions.get("z"))
    ret['sucess'] = True
    queue.put(ret)