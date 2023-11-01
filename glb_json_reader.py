import open3d as o3d
import json

# Load the JSON data from your file
with open('Baseflow/Unique.json', 'r') as file:
    data = json.load(file)

# Create a point cloud from the JSON data
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(data)

# Load the 3D model
glb_model_path = "Baseflow/fused.glb"  # Replace with the path to your glb model
mesh = o3d.io.read_triangle_mesh(glb_model_path)

# Create a new color for the entire mesh (e.g., blue)
new_color = [0.0, 0.0, 1.0]  # Blue color (RGB)

# Create an array of the same color for all vertices
colors = [new_color] * len(mesh.vertices)
mesh.vertex_colors = o3d.utility.Vector3dVector(colors)

# Create a visualization pipeline
vis = o3d.visualization.Visualizer()

# Add the point cloud and the mesh to the pipeline
vis.create_window()
vis.add_geometry(point_cloud)
vis.add_geometry(mesh)

# Optionally, you can specify transformations to position the geometries
# For example, to move the 3D model slightly up:
# mesh.translate([0, 0, 10])

# Run the visualization pipeline
vis.run()
vis.destroy_window()

