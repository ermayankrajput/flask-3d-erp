import trimesh
import os
from stltojpg import stlToImg
import requests


def meshRun(queue,fileServerPath):
    print(fileServerPath)
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

    if not os.path.exists('uploads/transported'):
        os.makedirs('uploads/transported')
    # Export the new mesh in the STL format
    mesh.export('uploads/transported/'+FileMainName+'--demo1.stl')
    # print("MESH CONVERTER", mesh.bounding_box())
    dimensions = stlToImg('uploads/transported/'+FileMainName+'--demo1.stl', 'uploads/images/'+FileMainName+'.stl.png')
    # print("Dimesions stltojpg ", dimensions)
    ret['converted_file'] = 'uploads/transported/'+FileMainName+'--demo1.stl'
    ret['image'] = 'uploads/images/'+FileMainName+'--demo1.stl.png'
    ret['x'] = str(dimensions.get("x"))
    ret['y'] = str(dimensions.get("y"))
    ret['z'] = str(dimensions.get("z"))
    ret['sucess'] = True
    queue.put(ret)