import os
# Force PyVista to use OSMesa for offscreen rendering
os.environ["PYVISTA_OFF_SCREEN"] = "true"
os.environ["PYVISTA_USE_MESA"] = "true"
import pyvista as pv
import numpy as np

def handle_stl_file(queue,fileServerPath):
    # Load STL file
    # ret = queue.get()
    # pv.OFF_SCREEN = True
    # pv.global_theme.off_screen = True
    # pv.start_xvfb()
    # Enable offscreen rendering
    pv.global_theme.off_screen = True
    mesh = pv.read(fileServerPath)

    # Compute bounding box dimensions
    bounds = mesh.bounds
    length = bounds[1] - bounds[0]
    width  = bounds[3] - bounds[2]
    height = bounds[5] - bounds[4]

    # Offscreen rendering with OSMesa
    plotter = pv.Plotter(off_screen=True, window_size=(250, 250))
    plotter.add_mesh(mesh, color='cyan', line_width=1, edge_color='r')
    plotter.hide_axes()

    # Screenshot
    screenshot_path = f"{fileServerPath}.jpg"
    plotter.screenshot(screenshot_path)
    plotter.close()

    # Return dimensions via queue
    queue.put((length, width, height))

    # Optionally retrieve result immediately (if needed)
    # result = queue.get()
    # return result

    # return (length,width,height)
# Example usage

# save_stl_image(fileServerPath)


