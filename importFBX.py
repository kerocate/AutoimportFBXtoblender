import bpy 
import sys
import os

def find_fbx(directory):
    print("Listing: " + directory)
    for file in os.listdir("."):
    	if file.endswith(".fbx"):
        	curr_fbx_file = file
        	print(curr_fbx_file)


    convert(curr_fbx_file, directory)

def convert(fbx_p,output_dir):
	fbx_path = os.path.join(output_dir, fbx_p)
	base, ext = os.path.splitext(fbx_p)
	bpy.ops.wm.read_homefile()
	bpy.ops.import_scene.fbx(filepath=fbx_path, axis_forward='-Z', axis_up='Y')

	return

if __name__ == "__main__":
	path_to_fbx_file_folders = "/Users/keroc/3D Objects/"

	files = folders = 0

	directories = [os.path.abspath(x[0]) for x in os.walk(path_to_fbx_file_folders)]
	directories.remove(os.path.abspath(path_to_fbx_file_folders)) # If you don't want your main directory included

	for i in directories:
		os.chdir(i)         # Change working Directory
		find_fbx(i)    
