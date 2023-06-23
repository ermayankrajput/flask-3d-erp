import trimesh
import os

def meshRun(queue,fileServerPath):
    fileNameSplit = fileServerPath.split("/")    
    FileMainName = fileNameSplit[len(fileNameSplit)-1]
    splitFile = FileMainName.split(".")
    splitFileFirstName = splitFile[len(splitFile)-2]
    ret = queue.get()
    mesh = trimesh.Trimesh(**trimesh.interfaces.gmsh.load_gmsh(fileServerPath, gmsh_args = [
                ("Mesh.Algorithm", 2), #Different algorithm types, check them out
                ("Mesh.CharacteristicLengthFromCurvature", 50), #Tuning the smoothness, + smothness = + time
                ("General.NumThreads", 10), #Multithreading capability
                ("Mesh.MinimumCirclePoints", 32)])) 
    print("Mesh volume: ", mesh.volume)
    # print("Mesh Bounding Box volume: ", mesh.bounding_box_oriented.volume)
    print("Mesh Area: ", mesh.area)

    if not os.path.exists('uploads/transported'):
        os.makedirs('uploads/transported')
    # Export the new mesh in the STL format
    mesh.export('uploads/transported/'+splitFileFirstName+'.stl')
    ret['foo'] = True
    ret['converted_file'] = 'uploads/transported/'+splitFileFirstName+'.stl'
    queue.put(ret)