import cv2
import numpy as np
import matplotlib.pyplot as plt

def generate_slope_field(image_path, step_size=10):
    # load img
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # detect edges
    edges = cv2.Canny(img, 50, 150)

    # calculate gradients
    dx, dy = np.gradient(edges)

    # normalize gradients
    magnitude = np.sqrt(dx**2 + dy**2)
    dx /= magnitude
    dy /= magnitude

    # create slope field
    x, y = np.meshgrid(np.arange(0, img.shape[1], step_size), np.arange(0, img.shape[0], step_size))

    fig = plt.figure(num="saber slope field")
    # plot slope field
    plt.quiver(x, y, dx[::step_size, ::step_size], dy[::step_size, ::step_size], scale=20)
    plt.imshow(img, cmap='gray')

    plt.show()

# replace file path accordingly
generate_slope_field("../images/saber.jpg")
