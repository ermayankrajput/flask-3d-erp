import trimesh
import os
from dimension import stlToImg

def meshRun(queue,fileServerPath):
    print(fileServerPath)
    ret = queue.get()
    mesh = trimesh.Trimesh(**trimesh.interfaces.gmsh.load_gmsh(fileServerPath, gmsh_args = [
                ("Mesh.Algorithm", 2), #Different algorithm types, check them out
                ("Mesh.CharacteristicLengthFromCurvature", 50), #Tuning the smoothness, + smothness = + time
                ("General.NumThreads", 20), #Multithreading capability
                ("Mesh.MinimumCirclePoints", 32)])) 
    mesh.export(fileServerPath + '.stl')
    ret['sucess'] = True
    queue.put(ret)