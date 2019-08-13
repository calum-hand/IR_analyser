import cv2
import matplotlib.pyplot as plt
import numpy as np


im = cv2.imread('test_ir.PNG')  # read image as numpy array

y_vals = []
x_vals = []

for row, i in enumerate(im):
    for column, j in enumerate(i):  # iterate over rows and columns
        for value in j:
            if value != 255:  # if the value is non white
                y_vals.append(row)
                x_vals.append(column)  # append value

y_vals = np.array(y_vals)  # convert to arrays
x_vals = np.array(x_vals)

sorted = np.argsort(x_vals)  # sort the x values to fix everything !!!!!!!
x = x_vals[sorted]  # resort
y = y_vals[sorted]  # resort


plt.plot(x[:5000], y[:5000], '.', label='first')  # PROOF
plt.plot(x[5000:10000], y[5000:10000], '.', label='second')
plt.plot(x[10000:15000], y[10000:15000], '.', label='third')
plt.plot(x[15000:], y[15000:], '.', label='fourth')
plt.legend()
plt.show()