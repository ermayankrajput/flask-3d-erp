import os
import pyvista as pv

def handle_stl_file(queue, fileServerPath):
    # --- Force full software/offscreen rendering ---
    os.environ["PYVISTA_OFF_SCREEN"] = "true"
    os.environ["PYVISTA_USE_MESA"] = "true"
    os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"
    os.environ["MESA_GL_VERSION_OVERRIDE"] = "3.3"
    os.environ["MESA_GLSL_VERSION_OVERRIDE"] = "330"
    os.environ["DISPLAY"] = ""

    # pv.OFF_SCREEN = True
    # pv.global_theme.off_screen = True

    # Optional: start virtual framebuffer (safe if already running)
    try:
        pv.start_xvfb(wait=1)
    except Exception:
        pass  # ignore if already running

    try:
        mesh = pv.read(fileServerPath)
    except Exception as e:
        queue.put(("Error", str(e)))
        return

    bounds = mesh.bounds
    length = bounds[1] - bounds[0]
    width = bounds[3] - bounds[2]
    height = bounds[5] - bounds[4]

    plotter = pv.Plotter(off_screen=True, window_size=(250, 250))
    plotter.add_mesh(mesh, color="cyan", line_width=1, edge_color="r")
    plotter.hide_axes()

    screenshot_path = f"{fileServerPath}.jpg"
    try:
        plotter.screenshot(screenshot_path)
    finally:
        plotter.close()

    queue.put((length, width, height))
