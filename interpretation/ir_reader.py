import numpy as np
import matplotlib.pyplot as plt
import cv2

im = cv2.imread('rough_ir.PNG')  # read and convert to numpy array
non_white = np.where(im != 255)  # find coordinates of non white cells
y, x, z = non_white  # unpack values (intentionally unpack as y, x, z due to how arrays are returned)

plt.plot(x[::10], y[::10], '.',  color='green')  # proof of extraction
plt.show()
