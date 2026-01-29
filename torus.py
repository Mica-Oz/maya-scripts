import maya.cmds as cmds
import math

# Torus shape
radius = 1.0
minor_radius = 0.7

# Diagonal density
sections = 11
spans = 12

# How many parallel lines do you want?
num_lines = 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

steps_to_close = (sections * spans) // gcd(sections, spans)

for line_num in range(num_lines):
    points = []
    offset = (line_num / float(num_lines)) * 2 * math.pi
    
    for i in range(steps_to_close):
        u = (i / float(sections)) * 2 * math.pi
        t = (i / float(spans)) * 2 * math.pi + offset
        
        x = (radius + minor_radius * math.cos(t)) * math.cos(u)
        y = minor_radius * math.sin(t)
        z = (radius + minor_radius * math.cos(t)) * math.sin(u)
        
        points.append((x, y, z))
    
    # Wrap points for periodic curve
    points = points + points[:3]
    
    # Create knots for periodic curve
    knots = list(range(len(points) + 3 - 1))
    
    curve = cmds.curve(p=points, degree=3, k=knots, per=True)
    cmds.rename(curve, "torusDiagonal_{}".format(line_num))

print("Done! Created {} lines".format(num_lines))