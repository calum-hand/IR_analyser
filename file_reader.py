import cv2
import matplotlib.pyplot as plt
import numpy as np

im = cv2.imread('test_ir.PNG')  # read image as numpy array
y, x, z = np.where(im < 245)  # get indices where the value is non white / white noise
sorted = np.argsort(x)  # sort the index values to read left to right top to bottom
x, y = x[sorted], y[sorted]  # re-sort

plt.plot(x[:5000], y[:5000], '.', label='first')  # PROOF
plt.plot(x[5000:10000], y[5000:10000], '.', label='second')
plt.plot(x[10000:15000], y[10000:15000], '.', label='third')
plt.plot(x[15000:], y[15000:], '.', label='fourth')
plt.legend()
plt.show()