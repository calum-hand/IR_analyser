import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.signal import find_peaks, argrelmax

plt.rcParams['figure.figsize'] = (15,5)

im = cv2.imread('rough_ir.PNG')  # read image and convert to numpy array
non_white = np.where(np.rot90(im,4) != 255)  # find coordinates of non white cells to extract plot
a, b, c = non_white  # unpack arrays



plt.plot(b, a, '.')
plt.scatter(1155,22, color='red', label='Array start (bottom right)')
plt.legend()
plt.savefig('created_images/plotted_as_b_a.PNG', bbox_inches='tight')
plt.show()

plt.plot(a, '.')
plt.legend()
plt.savefig('created_images/plot_of_a.PNG', bbox_inches='tight')
plt.show()

plt.plot(b, '.')
plt.legend()
plt.savefig('created_images/plot_of_b.PNG', bbox_inches='tight')
plt.show()