import meshio
import numpy as np
import matplotlib.pyplot as plt
# Test all
# Load the STL file
def stlToImg(stl_file="out.stl", image_file="file.png"):
    # stl_file = 'dragon.stl'  Replace with your STL file path
    mesh = meshio.read(stl_file)

    # Extract vertices and faces from the mesh data
    vertices = mesh.points
    faces = mesh.cells[0].data

    # Create a figure and plot the mesh
    fig = plt.figure()
    
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=faces)

    # Save the plot as an image
    # image_file = 'output.png'
    plt.savefig(image_file)
    plt.close()

    # Get dimensions of the mesh (bounding box)
    min_coords = np.min(vertices, axis=0)
    max_coords = np.max(vertices, axis=0)
    dimensions = max_coords - min_coords
    
    print("Dimensions (X, Y, Z):", dimensions)

    print("Image saved as:", image_file)
    return dimensions

