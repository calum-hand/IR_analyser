import numpy as np
import matplotlib.pyplot as plt
import cv2

########################################################################################################################


def peak_finder(data, n=10):
    """
    Similar to Scipy's find peaks function only this is cobbled together myself, and can hopefully apply it to my bugger
    of a problem (revise commenting).
    Checks all elements of a passed list and sees if they are the highest value in a +- n range, if yes then appends
    peak index to be returned
    :param data: list/array, 1D array of integers
    :param n: int, sets the range of the area for each data element to be compared against
    :return: list, indices of peak positions
    """
    peaks = []

    for d_index, i in enumerate(data):
        n_range = data[d_index - n : d_index + n]  # get index specific range of elements for comparison
        highest_peak = np.sum(i >= n_range)  # summaiton of booleans
        if highest_peak == 2 * n:  # if the peak is greater than or equal to (accounting for itself) 2 * range
            peaks.append(d_index)

    return peaks


########################################################################################################################






plt.rcParams['figure.figsize'] = (15,5)

im = cv2.imread('rough_ir.PNG')  # read image and convert to numpy array
non_white = np.where(im != 255)  # find coordinates of non white cells to extract plot
a, b, c = non_white  # unpack arrays


plt.subplot(131)
plt.plot(b[:50000:20], '.', color='blue')
plt.title('first half')
plt.ylim(0,1200)
plt.subplot(132)
plt.plot(b[50000::20], '.', color='red')
plt.title('second half')
plt.ylim(0,1200)
plt.subplot(133)
plt.plot(b[::20], '.', color='green')
plt.title('full')
plt.ylim(0,1200)
plt.savefig('created_images/proof_of_irregular_array_creation.PNG', bbox_inches='tight')
plt.show()
