import maya.cmds as cmds
import random
import math

def create_winding_circle(radius=1000, winding=5, irregularity=0.3, vertical_irregularity=0.2, num_points=100, seed=42, delete_previous=True, flatten_ends=False):
    """
    Create or update a randomly winding closed circle in Maya.
    """
    random.seed(seed)

    # Scale irregularity from [0,100] to [0,1] for calculation
    irregularity_scaled = irregularity / 100.0

    # Generate points for the curve
    points = []
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points * winding
        random_radius_offset = random.uniform(-1, 1) * irregularity_scaled
        distorted_radius = radius + random_radius_offset * radius
        x = distorted_radius * math.cos(angle)
        z = distorted_radius * math.sin(angle)
        y = random.uniform(-1, 1) * vertical_irregularity * radius
        
        if flatten_ends and (i == 0 or i == num_points - 1):
            y = 0  # Flatten the start and end points to y=0
        
        points.append((x, y, z))

    # Close the curve by appending the first point
    points.append((points[0][0], 0 if flatten_ends else points[0][1], points[0][2]))

    # Check if a previous curve exists and delete it if needed
    existing_curve = cmds.ls("winding_circle")
    if existing_curve and delete_previous:
        cmds.delete(existing_curve)
    
    # Create a new curve
    curve = cmds.curve(p=points, d=3, name="winding_circle")

def clamp_value(value, min_val, max_val, is_int=False):
    if is_int:
        return max(min_val, min(int(value), max_val))
    return max(min_val, min(float(value), max_val))

def show_ui():
    """
    Display the UI for controlling the winding circle parameters.
    """
    if cmds.window("WindingCircleUI", exists=True):
        cmds.deleteUI("WindingCircleUI")

    window = cmds.window("WindingCircleUI", title="Winding Circle Generator", widthHeight=(300, 400))
    cmds.columnLayout(adjustableColumn=True)

    # UI Controls
    cmds.text(label="Radius")
    radius_slider = cmds.floatSliderGrp(field=True, minValue=1.0, maxValue=5000.0, value=1000.0, fieldMinValue=1.0, fieldMaxValue=5000.0, precision=1, changeCommand=lambda _: update_curve())

    cmds.text(label="Winding")
    winding_slider = cmds.intSliderGrp(field=True, minValue=1, maxValue=20, value=5, fieldMinValue=1, fieldMaxValue=20, changeCommand=lambda _: update_curve())

    cmds.text(label="Irregularity")
    irregularity_slider = cmds.floatSliderGrp(field=True, minValue=0.0, maxValue=100.0, value=30.0, step=0.1, fieldMinValue=0.0, fieldMaxValue=100.0, precision=1, changeCommand=lambda _: update_curve())

    cmds.text(label="Vertical Irregularity")
    vertical_irregularity_slider = cmds.floatSliderGrp(field=True, minValue=0.0, maxValue=1.0, value=0.2, fieldMinValue=0.0, fieldMaxValue=1.0, precision=2, changeCommand=lambda _: update_curve())

    cmds.text(label="Number of Points")
    num_points_slider = cmds.intSliderGrp(field=True, minValue=10, maxValue=500, value=100, fieldMinValue=10, fieldMaxValue=500, changeCommand=lambda _: update_curve())

    cmds.text(label="Seed")
    seed_slider = cmds.intSliderGrp(field=True, minValue=1, maxValue=1000, value=42, fieldMinValue=1, fieldMaxValue=1000, changeCommand=lambda _: update_curve())
    
    delete_prev_check = cmds.checkBox(label="Delete Previous Curve", value=True)
    live_update_check = cmds.checkBox(label="Live Update", value=False)
    flatten_ends_check = cmds.checkBox(label="Flatten Curve Ends to y=0", value=False, changeCommand=lambda _: update_curve())

    def update_curve(*args):
        radius = clamp_value(cmds.floatSliderGrp(radius_slider, query=True, value=True), 1.0, 5000.0)
        winding = clamp_value(cmds.intSliderGrp(winding_slider, query=True, value=True), 1, 20, True)
        irregularity = clamp_value(cmds.floatSliderGrp(irregularity_slider, query=True, value=True), 0.0, 100.0)
        vertical_irregularity = clamp_value(cmds.floatSliderGrp(vertical_irregularity_slider, query=True, value=True), 0.0, 1.0)
        num_points = clamp_value(cmds.intSliderGrp(num_points_slider, query=True, value=True), 10, 500, True)
        seed = clamp_value(cmds.intSliderGrp(seed_slider, query=True, value=True), 1, 1000, True)
        delete_previous = cmds.checkBox(delete_prev_check, query=True, value=True)
        flatten_ends = cmds.checkBox(flatten_ends_check, query=True, value=True)
        create_winding_circle(radius, winding, irregularity, vertical_irregularity, num_points, seed, delete_previous, flatten_ends)
    
    cmds.button(label="Create", command=update_curve)
    cmds.showWindow(window)

# Show the UI
show_ui()
