import cv2
import numpy as np
import matplotlib.pyplot as plt

def generate_slope_field(image_path, step_size=10):
    # Load the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Canny edge detection
    edges = cv2.Canny(img, 50, 150)

    # Calculate gradients
    dx, dy = np.gradient(edges)

    # Normalize gradients
    magnitude = np.sqrt(dx**2 + dy**2)
    dx /= magnitude
    dy /= magnitude

    # Create slope field
    x, y = np.meshgrid(np.arange(0, img.shape[1], step_size), np.arange(0, img.shape[0], step_size))

    fig = plt.figure(num="saber slope field")
    # Plot slope field
    plt.quiver(x, y, dx[::step_size, ::step_size], dy[::step_size, ::step_size], scale=20)
    plt.imshow(img, cmap='gray')

    # Show the plot
    plt.show()

# Example usage
generate_slope_field("../saber.jpg")
