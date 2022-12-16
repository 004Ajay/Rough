# Python script to make random spheres in x, y, z axes in blender

import bpy
import random

for i in range(50): # Create 50 spheres
    x = y = z = random.uniform(-100, 100) # Generate a random position in x, y, z axes

    # Create a sphere at the random position
    bpy.ops.mesh.primitive_uv_sphere_add(location=(x, y, z), radius=5)