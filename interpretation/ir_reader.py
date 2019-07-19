import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.signal import find_peaks

plt.rcParams['figure.figsize'] = (15,5)

im = cv2.imread('rough_ir.PNG')  # read image and convert to numpy array
non_white = np.where(im != 255)  # find coordinates of non white cells to extract plot
a, b, c = non_white  # unpack arrays


plt.subplot(131)
plt.plot(b[:50000], '.', color='blue')
plt.title('first half')
plt.subplot(132)
plt.plot(b[50000:], 'x', color='red')
plt.title('second half')
plt.subplot(133)
plt.plot(b, 'x', color='green')
plt.title('full')
plt.savefig('created_images/proof_of_irregular_array_creation.PNG', bbox_inches='tight')
plt.show()
