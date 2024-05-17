import pyvista as pv

fileServerPath = "dragon.stl"
output_file = 'object_image4.jpg'
def save_stl_image(queue,fileServerPath):
    # Load STL file
    # ret = queue.get()
    mesh = pv.read(fileServerPath)

    # Get object dimensions using bounding box
    bounds = mesh.bounds
    length = bounds[1] - bounds[0]
    width = bounds[3] - bounds[2]
    height = bounds[5] - bounds[4]
    # print(f"Object dimensions (length, width, height): {length}, {width}, {height}")


    # Render the mesh
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh, color='cyan', line_width=1, edge_color='r')
    plotter.hide_axes()

    plotter.window_size = (250, 250)

    # Save image
    plotter.screenshot(fileServerPath + ".jpg")
    plotter.close()
    # ret['sucess'] = True
    queue.put((length,width,height))
    result = queue.get()

    # return (length,width,height)
# Example usage

# save_stl_image(fileServerPath)


