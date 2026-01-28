# Torus Spiral Generator

A Maya Python script that generates a spiral curve wound around a NURBS torus using parametric equations.

## Prerequisites

- Autodesk Maya (with `maya.cmds`)
- A NURBS torus in your scene (default name: `nurbsTorus1`)

## Usage

1. Create a NURBS torus in Maya (`Create > NURBS Primitives > Torus`).
2. Run the script in Maya's Script Editor (Python tab).

The script reads the torus's `radius` and `sectionRadius` from the `makeNurbTorus1` construction history node and generates a spiral curve that wraps around the torus surface.

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `loops` | `15` | Number of times the spiral winds around the tube |
| `torus_name` | `"nurbsTorus1"` | Name of the torus object in the scene |
| `points_per_loop` | `100` | Number of points per loop (controls smoothness) |

## Output

Creates a degree-3 NURBS curve named `torusSpiral` that follows the surface of the torus.
