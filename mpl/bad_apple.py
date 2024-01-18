import os
import re
import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames_folder = 'frames'
frame_files = sorted(os.listdir(frames_folder), key=lambda x: int(re.search(r'\d+', x).group()))

def update(frame):
    plt.clf()  # clear fig
    frame_path = os.path.join(frames_folder, frame_files[frame])

    # detect edges 
    frame_image = cv2.imread(frame_path, cv2.IMREAD_GRAYSCALE) 
    edges = cv2.Canny(frame_image, 50, 150)

    # render frame
    plt.imshow(edges, cmap='gray')
    plt.title(f'Frame {frame + 1}/{len(frame_files)}')

fig, ax = plt.subplots(num="Bad Apple")

animation = FuncAnimation(fig, update, frames=len(frame_files), interval=5)

plt.show()