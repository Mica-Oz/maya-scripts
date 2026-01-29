# Torus Diagonal Curve Generator

A Maya Python script that generates diagonal curves wound around a torus using parametric equations.

## Prerequisites

- Autodesk Maya (with `maya.cmds`)

## Usage

Run the script in Maya's Script Editor (Python tab). It creates closed periodic curves that wrap diagonally around a torus shape.

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `sections` | `11` | Change the diagonal angle and density |
| `spans` | `12` | Change the diagonal angle and density |
| `minor_radius` | `0.7` | Tighten or loosen the hole |
| `num_lines` | `1` | Add more parallel lines to fill it out |
| `radius` | `1.0` | Scale the whole thing up/down |

## Output

Creates degree-3 periodic NURBS curves named `torusDiagonal_0`, `torusDiagonal_1`, etc.
