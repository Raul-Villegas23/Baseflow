import open3d as o3d
import numpy as np

print("Load a glb 3D model with colors, print it, and render it")
glb_model_path = "Baseflow/fused.glb"  # Replace with the path to your glb model

# Read the glb model
mesh = o3d.io.read_triangle_mesh(glb_model_path)

# Create a new color for the entire mesh (e.g., blue)
new_color = [0.0, 0.0, 0.8]  # Blue color (RGB)

# Create an array of the same color for all vertices
colors = np.array([new_color] * len(mesh.vertices))

# Set the new color array as vertex colors
mesh.vertex_colors = o3d.utility.Vector3dVector(colors)

print(mesh)

# Create a visualization window
vis = o3d.visualization.Visualizer()

# Add the mesh with colors to the visualization
vis.create_window()
vis.add_geometry(mesh)
vis.run()
vis.destroy_window()


