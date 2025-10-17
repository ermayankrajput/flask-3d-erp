import os
import pyvista as pv

def handle_stl_file(queue, fileServerPath):
    os.environ["PYVISTA_OFF_SCREEN"] = "true"
    os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"
    pv.global_theme.off_screen = True

    mesh = pv.read(fileServerPath)

    bounds = mesh.bounds
    length = bounds[1] - bounds[0]
    width  = bounds[3] - bounds[2]
    height = bounds[5] - bounds[4]

    plotter = pv.Plotter(off_screen=True, window_size=(250, 250))
    plotter.add_mesh(mesh, color="cyan", line_width=1, edge_color="r")
    plotter.hide_axes()

    plotter.screenshot(f"{fileServerPath}.jpg")
    plotter.close()

    queue.put((length, width, height))
