import cv2
import numpy as np
import json


def map_black_pixels(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply edge detection using Canny
    edges = cv2.Canny(img, 30, 100)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Map black pixels to x-y coordinates
    black_pixel_coords = []
    for contour in contours:
        for point in contour:
            x, y = point[0]
            black_pixel_coords.append({"x": x, "y": y})

    
    # convert to meter scale
    scale_factor = 10

    max_x = max(coord["x"] for coord in black_pixel_coords)
    max_y = max(coord["y"] for coord in black_pixel_coords)

    scaled_coords = [{"x": coord["x"] * scale_factor / max_x, "y": coord["y"] * scale_factor / max_y}
                     for coord in black_pixel_coords]

    return scaled_coords

# Replace 'your_image_path.jpg' with the path to your image file
image_path = 'your_image_path.jpg'
coords = map_black_pixels(image_path)

# Replace 'path.json' with the name of your PathPlanner JSON file (change .path to .JSON if doesn't work)
# Copy and paste the contents of path.json into your PathPlanner JSON file (it can't be empty)

with open('path.json', 'r') as file:
    path_planner_data = json.load(file)

new_waypoints = []
for i, coord in enumerate(coords):
    adjusted_y = coord["y"] - 1.75

    waypoint = {
        "anchor": {"x": coord["x"], "y": adjusted_y},
        "prevControl": None if i == 0 else {"x": coords[i-1]["x"], "y": adjusted_y},
        "nextControl": None if i == len(coords) - 1 else {"x": coords[i+1]["x"], "y": adjusted_y},
        "isLocked": False,
        "linkedName": None
    }
    new_waypoints.append(waypoint)

path_planner_data["waypoints"] = new_waypoints
with open('generate.json', 'w') as file:
    json.dump(path_planner_data, file, indent=2)
