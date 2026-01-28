import maya.cmds as cmds
import math

# Parameters
loops = 15  # how many times it winds around the tube
torus_name = "nurbsTorus1"  # change if your torus has a different name
points_per_loop = 100  # smoothness

# Get torus dimensions from the makeNurbTorus node
radius = cmds.getAttr("makeNurbTorus1.radius")
section_radius = cmds.getAttr("makeNurbTorus1.sectionRadius")

# Generate spiral points
points = []
total_points = loops * points_per_loop

for i in range(total_points + 1):
    t = (i / total_points) * loops * 2 * math.pi  # angle around tube
    u = (i / total_points) * 2 * math.pi  # angle around torus center
    
    # Torus parametric equations with spiral
    x = (radius + section_radius * math.cos(t)) * math.cos(u)
    y = section_radius * math.sin(t)
    z = (radius + section_radius * math.cos(t)) * math.sin(u)
    
    points.append((x, y, z))

# Create the curve
curve = cmds.curve(p=points, degree=3)
cmds.rename(curve, "torusSpiral")
print("Created spiral with {} loops".format(loops))