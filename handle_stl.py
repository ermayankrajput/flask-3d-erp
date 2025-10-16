import os
os.environ["PYVISTA_OFF_SCREEN"] = "true"
os.environ["PYVISTA_USE_OSMESA"] = "true"
os.environ["VTK_DEFAULT_RENDER_WINDOW_OFFSCREEN"] = "true"
import pyvista as pv

def handle_stl_file(queue,fileServerPath):
    # Load STL file
    # ret = queue.get()
    # pv.OFF_SCREEN = True
    # pv.global_theme.off_screen = True
    # pv.start_xvfb()
    # Enable offscreen rendering
    pv.global_theme.off_screen = True

    # Load STL
    mesh = pv.read(fileServerPath)

    # Compute object dimensions
    bounds = mesh.bounds
    length = bounds[1] - bounds[0]
    width = bounds[3] - bounds[2]
    height = bounds[5] - bounds[4]

    # Setup plotter for offscreen rendering
    plotter = pv.Plotter(off_screen=True, window_size=(250, 250))
    plotter.add_mesh(mesh, color='cyan', line_width=1, edge_color='r')
    plotter.hide_axes()

    # Save screenshot
    output_file = fileServerPath + ".jpg"
    plotter.screenshot(output_file)
    plotter.close()

    # Send dimensions back via queue
    queue.put((length, width, height))

    # Optionally retrieve result immediately (if needed)
    # result = queue.get()
    # return result

    # return (length,width,height)
# Example usage

# save_stl_image(fileServerPath)


