# Python script to clear all objects in blender environment

import bpy

# Remove all objects
for obj in bpy.data.objects:
    bpy.data.objects.remove(obj, do_unlink=True)


"""
# use this script to clear other types of data in Blender, such as meshes, materials, and textures. 

import bpy

# Remove all meshes
for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(mesh, do_unlink=True)

"""