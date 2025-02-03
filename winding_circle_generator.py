import maya.cmds as cmds
import random
import math

def create_winding_circle(radius=100, winding=5, irregularity=0.3, vertical_irregularity=0.2, seed=42):
    """
    Create a randomly winding closed circle in Maya.
    
    Parameters:
    - radius (float): Base radius of the circle.
    - winding (int): Number of winding loops around the circle.
    - irregularity (float): Amount of random distortion for the radius (0 to 1).
    - vertical_irregularity (float): Amount of random distortion for the vertical movement (0 to 1).
    - seed (int): Random seed for repeatable results.
    """
    random.seed(seed)

    # Calculate number of points based on winding
    num_points = 100
    points = []

    for i in range(num_points):
        # Calculate the angle for each point
        angle = 2 * math.pi * i / num_points * winding
        # Add irregularity to radius
        random_radius_offset = random.uniform(-1, 1) * irregularity
        distorted_radius = radius + random_radius_offset * radius
        # Calculate the x, z coordinates
        x = distorted_radius * math.cos(angle)
        z = distorted_radius * math.sin(angle)
        # Add random vertical offset for organic up-and-down movement
        y = random.uniform(-1, 1) * vertical_irregularity * radius
        points.append((x, y, z))

    # Close the circle by appending the first point
    points.append(points[0])

    # Create a curve in Maya from the points
    curve = cmds.curve(p=points, d=3)
    cmds.rename(curve, "winding_circle")

def show_ui():
    """
    Display the UI for controlling the winding circle parameters.
    """
    if cmds.window("WindingCircleUI", exists=True):
        cmds.deleteUI("WindingCircleUI")

    window = cmds.window("WindingCircleUI", title="Winding Circle Generator", widthHeight=(300, 300))
    cmds.columnLayout(adjustableColumn=True)

    # Radius slider
    cmds.text(label="Radius")
    radius_slider = cmds.floatSliderGrp(field=True, minValue=1.0, maxValue=9999.0, value=100.0)

    # Winding slider
    cmds.text(label="Winding")
    winding_slider = cmds.intSliderGrp(field=True, minValue=1, maxValue=20, value=5)

    # Irregularity slider
    cmds.text(label="Irregularity")
    irregularity_slider = cmds.floatSliderGrp(field=True, minValue=0.0, maxValue=1.0, value=0.3)

    # Vertical Irregularity slider
    cmds.text(label="Vertical Irregularity")
    vertical_irregularity_slider = cmds.floatSliderGrp(field=True, minValue=0.0, maxValue=1.0, value=0.2)

    # Seed slider
    cmds.text(label="Seed")
    seed_slider = cmds.intSliderGrp(field=True, minValue=1, maxValue=1000, value=42)

    # Create button
    def on_create(*args):
        radius = cmds.floatSliderGrp(radius_slider, query=True, value=True)
        winding = cmds.intSliderGrp(winding_slider, query=True, value=True)
        irregularity = cmds.floatSliderGrp(irregularity_slider, query=True, value=True)
        vertical_irregularity = cmds.floatSliderGrp(vertical_irregularity_slider, query=True, value=True)
        seed = cmds.intSliderGrp(seed_slider, query=True, value=True)
        create_winding_circle(radius, winding, irregularity, vertical_irregularity, seed)

    cmds.button(label="Create", command=on_create)

    # Show the window
    cmds.showWindow(window)

# Show the UI
show_ui()
