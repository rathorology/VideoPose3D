import numpy as np
from numpy import load

path = "/home/rathorology/PycharmProjects/VideoPose3D/output_directory/1.mp4/keypoints.npy"
k = np.load(path, allow_pickle=True)

print(k)
