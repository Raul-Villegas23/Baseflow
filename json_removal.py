import json

# Load the JSON data from your file
with open('Baseflow/Vertices.json', 'r') as file:
    data = json.load(file)

# Create a list to store unique points
unique_data = []

# Iterate through the points in the JSON data and add them to the list if they are unique
for point in data:
    if point not in unique_data:
        unique_data.append(point)

# Save the unique data back to a JSON file with the same format
with open('Baseflow/unique.json', 'w') as file:
    json.dump(unique_data, file, indent=4)

