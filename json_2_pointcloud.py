import open3d as o3d
import json

# Load the JSON data from your file
with open('Baseflow/Vertices.json', 'r') as file:
    data = json.load(file)

# Create a point cloud from the JSON data
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(data)

# Create a visualization window
o3d.visualization.draw_geometries([point_cloud])
