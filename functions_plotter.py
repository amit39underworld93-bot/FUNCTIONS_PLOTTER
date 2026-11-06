import numpy as np
import matplotlib.pyplot as plt
import sys

try:
    dimension = int(input("Enter the dimension between 1 and 3: "))
except Exception:
    print("INVALID INPUT! Please enter a valid numeric value between 1 and 3!!!")
    sys.exit()

if dimension < 1 or dimension > 3:
    print("Please enter a valid dimension between 1 and 3: ")
    sys.exit()

allowed = {
    "x" : None, 
    "y" : None,
    "z" : None,
    "sin" : np.sin,
    "cos" : np.cos,
    "tan" : np.tan,
    "sqrt" : np.sqrt,
    "arcsin" : np.arcsin,   
    "arccos" : np.arccos,
    "arctan" : np.arctan,
    "log" : np.log,
    "exp" : np.exp,
    "pi" : np.pi,
    "e" : np.e, 
    "sinh" : np.sinh, 
    "cosh" : np.cosh, 
    "tanh" : np.tanh,
    "log10" : np.log10, 
    "abs" : np.abs, 
    "floor" : np.floor, 
    "ceil" : np.ceil
}

if dimension == 1:

    expression = input("Enter the function f(x): ")

    try:
        x_min = float(input("Enter the minimum value for x: "))
        x_max = float(input("Enter the maximum value for x: "))
    except ValueError:
        print("INVALID INPUT! Please enter valid numeric value for x!!!")
        sys.exit()

    if x_min >= x_max:
        print("INVALID RANGE!!! \nMinimum x cannot be greater than maximum x!!!")
        sys.exit()

    try:
        resolution = int(input("Enter the number of resolutions for x: "))
    except Exception:
        print("Resolution must be an integer!!!")
        sys.exit()

    if resolution <= 0:
        print("Number of resolutions must be greater than zero!!!")
        sys.exit()

    def f(x):
        values = allowed.copy()
        values["x"] = x

        with np.errstate(all = "ignore"):
            y = eval(expression, {"__builtins__": {}}, values)
            if isinstance(y, (int, float)):
                y = y*np.ones_like(x)

        valid = np.isfinite(y)

        if not np.any(valid):
            print("Function produced no valid values in the given range!!!")
            sys.exit()

        y[~valid] = np.nan

        difference = np.abs(np.diff(y))

        finite_difference = difference[np.isfinite(difference)]

        if len(finite_difference) > 0:
            median_difference = np.median(finite_difference)
        else:
            median_difference = 0

        if median_difference > 0:
            threshold = 100*median_difference

            jump = difference > threshold
            y[:-1][jump] = np.nan
            y[1:][jump] = np.nan

        return y

    x = np.linspace(x_min, x_max, resolution)

    try: 
        y = f(x)
    except Exception:
        print("Please enter a valid function!!!")
        sys.exit()

    plt.plot(x, y, label = f"function: {expression}")

    plt.axhline(0, color = "black")
    plt.axvline(0, color = "black")

    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("FUNCTIONS PLOTTER", color = "maroon")

    plt.legend()
    plt.grid()
    plt.show()

elif dimension == 2:

    expression = input("Enter the function f(x, y): ")

    try:
        x_min = float(input("Enter the minimum value for x: "))
        x_max = float(input("Enter the maximum value for x: "))

    except ValueError:
        print("INVALID INPUT! Please enter valid numeric values for x!!!")
        sys.exit()


    try:
        y_min = float(input("Enter the minimum value for y: "))
        y_max = float(input("Enter the maximum value for y: "))
    except ValueError:
        print("INVALID INPUT! Please enter a valid numeric value for y!!!")
        sys.exit()

    if x_min >= x_max:
        print("INVALID RANGE!!! \nMinimum x cannot be greater than maximum x!!!")
        sys.exit()

    if y_min >= y_max:
        print("INVALID RANGE!!! \nMinimum y cannot be greater than maximum y!!!")
        sys.exit()

    try:
        resolution = int(input("Enter the number of resolutions for both x and y: "))
    except ValueError:
        print("Resolution must be an integer!!!")
        sys.exit()

    if resolution <= 0:
        print("Number of resolutions must be greater than zero!!!")
        sys.exit()

    if resolution < 50 or resolution > 2000:
        print("Resolution must be between 50 and 2000!!!")
        sys.exit()

    def f(x, y):
        values = allowed.copy()
        values["x"] = x
        values["y"] = y

        with np.errstate(all = "ignore"):
            result = eval(expression, {"__builtins__": {}}, values)
            if isinstance(result, (int, float)):
                result = result*np.ones_like(x)


        return result

    x = np.linspace(x_min, x_max, resolution)
    y = np.linspace(y_min, y_max, resolution)

    X, Y = np.meshgrid(x, y)

    try:
        F = f(X, Y)
    except Exception:
        print("Please enter a valid function!!!")
        sys.exit()

    valid = np.isfinite(F)
    if not np.any(valid):
        print("Function produced no valid values in the given range!!!")
        sys.exit()

    F[~valid] = np.nan

    if np.nanmin(F) > 0 or np.nanmax(F) < 0:
        print("No real curve is found in the given range!!!")
        sys.exit()

    contour = plt.contour(X, Y, F, levels = [0], colors = "blue")

    plt.axis("equal")

    plt.axhline(0, color = "black")
    plt.axvline(0, color = "black")

    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title(f"f(x, y) = {expression}", color = "maroon")

    plt.grid(linestyle = "--")
    plt.show()

else:

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = "3d")

    expression = input("Enter the function f(x, y, z): ")

    try:
        x_min = float(input("Enter the minimum value for x: "))
        x_max = float(input("Enter the maximum value for x: "))

    except ValueError:
        print("INVALID INPUT! Please enter valid numeric values for x!!!")
        sys.exit()


    try:
        y_min = float(input("Enter the minimum value for y: "))
        y_max = float(input("Enter the maximum value for y: "))
    except ValueError:
        print("INVALID INPUT! Please enter a valid numeric value for y!!!")
        sys.exit()

    try:
        z_min = float(input("Enter the minimum value for z: "))
        z_max = float(input("Enter the maximum value for z: "))
    except ValueError:
        print("INVALID INPUT! Please enter a valid numeric value for z!!!")
        sys.exit()

    if x_min >= x_max:
        print("INVALID RANGE!!! \nMinimum x cannot be greater than maximum x!!!")
        sys.exit()

    if y_min >= y_max:
        print("INVALID RANGE!!! \nMinimum y cannot be greater than maximum y!!!")
        sys.exit()

    if z_min >= z_max:
        print("INVALID RANGE!!! \nMinimum z cannot be greater than maximum z!!!")
        sys.exit()

    try:
        resolution = int(input("Enter the number of resolutions for both x, y and z: "))
    except ValueError:
        print("Resolution must be an integer!!!")
        sys.exit()

    if resolution <= 0:
        print("Number of resolutions must be greater than zero!!!")
        sys.exit()

    if resolution < 50 or resolution > 150:
        print("Resolution must be between 50 and 150!!!")
        sys.exit()

    def f(x, y, z):
        values = allowed.copy()
        values["x"] = x
        values["y"] = y
        values["z"] = z

        with np.errstate(all = "ignore"):
            result = eval(expression, {"__builtins__": {}}, values)
            if isinstance(result, (int, float)):
                result = result*np.ones_like(x)

        return result

    x = np.linspace(x_min, x_max, resolution)
    y = np.linspace(y_min, y_max, resolution)
    z = np.linspace(z_min, z_max, resolution)

    X, Y, Z = np.meshgrid(x, y, z, indexing = "ij")

    try:
        F = f(X, Y, Z)
    except Exception:
        print('''
    Invalid Function!!!
    Please check: 
    - Variable names: x, y, z
    - Mathematical syntax
    - Supported functions
    ''')
        sys.exit()

    valid = np.isfinite(F)

    if not np.any(valid):
        print("Function produced no valid value in the given range!!!")
        sys.exit()

    if not np.all(valid):
        print("Function produced undefined values in the given range!!!")
        print("Please choose a different range or modify the given function!!!")
        sys.exit()

    if np.min(F) > 0 or np.max(F) < 0:
        print("No real surface is found in the given range!!!")
        sys.exit()

    try:
        from skimage.measure import marching_cubes
    except ImportError:
        print("scikit-image is required for 3D implicit plotting!!!")
        print("\nInstall it using:")
        print("\npip install scikit-image")
        sys.exit()

    try:
        vertices, faces, normals, values = marching_cubes(F, level = 0)
    except RuntimeError:
        print("No surface found for f(x, y, z) = 0 in the given range!!!")
        sys.exit()

    vertices[:, 0] = np.interp(vertices[:, 0], np.arange(resolution), x)
    vertices[:, 1] = np.interp(vertices[:, 1], np.arange(resolution), y)
    vertices[:, 2] = np.interp(vertices[:, 2], np.arange(resolution), z)

    ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=faces, alpha=0.7)

    ax.set_title(f"3D FUNCTIONS PLOTTER\nf(x, y, z) = {expression}", color = "maroon", weight = "bold")

    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_zlabel("z-axis")

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_zlim(z_min, z_max)

    ax.view_init(elev = 25, azim = 45)

    ax.set_box_aspect((1, 1, 1))

    plt.tight_layout()

    plt.grid(linestyle = "--")
    plt.show()