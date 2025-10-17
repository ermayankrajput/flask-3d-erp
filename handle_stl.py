import os
import pyvista as pv
import numpy as np

# Global environment setup for off-screen rendering under xvfb
os.environ["PYVISTA_OFF_SCREEN"] = "true"
os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"
os.environ["MESA_GL_VERSION_OVERRIDE"] = "3.3"
os.environ["MESA_GLSL_VERSION_OVERRIDE"] = "330"

# Global PyVista setup
pv.global_theme.off_screen = True

def handle_stl_file(queue, fileServerPath):
    """
    Load an STL file, compute its bounding-box dimensions,
    render a 250x250px preview image off-screen,
    and return the dimensions via the provided multiprocessing.Queue.
    """

    try:
        # Read STL
        mesh = pv.read(fileServerPath)

        # Compute dimensions
        bounds = mesh.bounds
        length = bounds[1] - bounds[0]
        width  = bounds[3] - bounds[2]
        height = bounds[5] - bounds[4]

        # Create offscreen plotter
        plotter = pv.Plotter(off_screen=True, window_size=(250, 250))
        plotter.add_mesh(mesh, color="cyan", line_width=1, edge_color="r")
        plotter.hide_axes()

        # Save screenshot
        screenshot_path = f"{fileServerPath}.jpg"
        plotter.screenshot(screenshot_path)

        # Close plotter to free memory
        plotter.close()

        # Return via queue
        queue.put((length, width, height))

    except Exception as e:
        queue.put(("Error", str(e)))
