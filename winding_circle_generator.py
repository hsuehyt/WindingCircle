import maya.cmds as cmds
import random
import math

def create_winding_circle(radius=100, winding=5, irregularity=0.3, vertical_irregularity=0.2, num_points=100, seed=42, delete_previous=True):
    """
    Create or update a randomly winding closed circle in Maya.
    """
    random.seed(seed)

    # Generate points for the curve
    points = []
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points * winding
        random_radius_offset = random.uniform(-1, 1) * irregularity
        distorted_radius = radius + random_radius_offset * radius
        x = distorted_radius * math.cos(angle)
        z = distorted_radius * math.sin(angle)
        y = random.uniform(-1, 1) * vertical_irregularity * radius
        points.append((x, y, z))

    # Close the curve by appending the first point
    points.append(points[0])

    # Check if a previous curve exists and delete it if needed
    existing_curve = cmds.ls("winding_circle")
    if existing_curve and delete_previous:
        cmds.delete(existing_curve)
    
    # Create a new curve
    curve = cmds.curve(p=points, d=3, name="winding_circle")

def show_ui():
    """
    Display the UI for controlling the winding circle parameters.
    """
    if cmds.window("WindingCircleUI", exists=True):
        cmds.deleteUI("WindingCircleUI")

    window = cmds.window("WindingCircleUI", title="Winding Circle Generator", widthHeight=(300, 350))
    cmds.columnLayout(adjustableColumn=True)

    # UI Controls
    cmds.text(label="Radius")
    radius_slider = cmds.floatSliderGrp(field=True, minValue=1.0, maxValue=1000.0, value=100.0)

    cmds.text(label="Winding")
    winding_slider = cmds.intSliderGrp(field=True, minValue=1, maxValue=20, value=5)

    cmds.text(label="Irregularity")
    irregularity_slider = cmds.floatSliderGrp(field=True, minValue=0.0, maxValue=1.0, value=0.3)

    cmds.text(label="Vertical Irregularity")
    vertical_irregularity_slider = cmds.floatSliderGrp(field=True, minValue=0.0, maxValue=1.0, value=0.2)

    cmds.text(label="Number of Points")
    num_points_slider = cmds.intSliderGrp(field=True, minValue=10, maxValue=500, value=100)

    cmds.text(label="Seed")
    seed_slider = cmds.intSliderGrp(field=True, minValue=1, maxValue=1000, value=42)
    
    delete_prev_check = cmds.checkBox(label="Delete Previous Curve", value=True)
    live_update_check = cmds.checkBox(label="Live Update", value=False)

    def update_curve(*args):
        radius = cmds.floatSliderGrp(radius_slider, query=True, value=True)
        winding = cmds.intSliderGrp(winding_slider, query=True, value=True)
        irregularity = cmds.floatSliderGrp(irregularity_slider, query=True, value=True)
        vertical_irregularity = cmds.floatSliderGrp(vertical_irregularity_slider, query=True, value=True)
        num_points = cmds.intSliderGrp(num_points_slider, query=True, value=True)
        seed = cmds.intSliderGrp(seed_slider, query=True, value=True)
        delete_previous = cmds.checkBox(delete_prev_check, query=True, value=True)
        create_winding_circle(radius, winding, irregularity, vertical_irregularity, num_points, seed, delete_previous)
    
    def on_create(*args):
        update_curve()
    
    def on_reset(*args):
        cmds.floatSliderGrp(radius_slider, edit=True, value=100.0)
        cmds.intSliderGrp(winding_slider, edit=True, value=5)
        cmds.floatSliderGrp(irregularity_slider, edit=True, value=0.3)
        cmds.floatSliderGrp(vertical_irregularity_slider, edit=True, value=0.2)
        cmds.intSliderGrp(num_points_slider, edit=True, value=100)
        cmds.intSliderGrp(seed_slider, edit=True, value=42)
        cmds.checkBox(delete_prev_check, edit=True, value=True)
        cmds.checkBox(live_update_check, edit=True, value=False)

    cmds.button(label="Create", command=on_create)
    cmds.button(label="Reset", command=on_reset)

    def check_live_update(*args):
        if cmds.checkBox(live_update_check, query=True, value=True):
            update_curve()
    
    # Attach live update to sliders
    cmds.floatSliderGrp(radius_slider, edit=True, dragCommand=check_live_update)
    cmds.intSliderGrp(winding_slider, edit=True, dragCommand=check_live_update)
    cmds.floatSliderGrp(irregularity_slider, edit=True, dragCommand=check_live_update)
    cmds.floatSliderGrp(vertical_irregularity_slider, edit=True, dragCommand=check_live_update)
    cmds.intSliderGrp(num_points_slider, edit=True, dragCommand=check_live_update)
    cmds.intSliderGrp(seed_slider, edit=True, dragCommand=check_live_update)

    cmds.showWindow(window)

# Show the UI
show_ui()