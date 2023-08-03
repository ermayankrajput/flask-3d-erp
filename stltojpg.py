import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
# from matplotlib import pylab
# from pylab import *

# Create a new plot
def stlToImg(inputStl="out.stl", outputImg="file.png"):
    # figure = pyplot.figure()
    # axes = figure.add_subplot(projection='3d')

    # Load the STL files and add the vectors to the plot
    your_mesh = mesh.Mesh.from_file(inputStl)
    # axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
    # Auto scale to the mesh size
    # scale = your_mesh.points.flatten()
    # axes.auto_scale_xyz(scale, scale, scale)
    # pylab.savefig('foo.png')

    # Show the plot to the screen
    # pyplot.show()
    meshDimension = {
                        'x': your_mesh.x.max() - your_mesh.x.min(),
                        'y': your_mesh.y.max() - your_mesh.y.min(),
                        'z': your_mesh.z.max() - your_mesh.z.min()
                    }
    # pyplot.savefig(outputImg, dpi='figure', format=None, metadata=None,
    #         bbox_inches=None, pad_inches=0.1,
    #         facecolor=None, edgecolor=None,
    #         backend=None, transparent=True)
    return meshDimension