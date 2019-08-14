import cv2
import numpy as np
from scipy.signal import find_peaks

########################################################################################################################


def spectrum_image_data(path_to_image):
    """
    Translates the passed IR spectrum image into an ordered numpy array. Only non white cells are considerd however the
    np.where filtering also removes some white noise by filtering based on < 245 rather than just != 255

    :param path_to_image: str, file path to the ir spectrum image to be analysed

    :return: numpy.ndarray, the sequential intensity values of the retrieved IR data
    """
    im = cv2.imread(path_to_image)  # read image as numpy array
    rgb_filter_value = 245
    y, x, z = np.where(im < rgb_filter_value)  # get indices where the value is non white / white noise
    sorted = np.argsort(x)  # sort the index values to read left to right top to bottom
    y = y[sorted]  # re-sort
    return y


########################################################################################################################

def ir_peak_locator(data, range_min, range_max):
    """
    Normalises the IR data extracted from the image previously to the wavenumber range of the IR spectrum itself.
    This assumes a linear scale across the entirety of the original IR spectrum, finds relative percentages of the peak
    locations and translates that to the original wavenumber range.

    To ensure a suitable number of peaks are found and to prevent noisy peaks from being flagged, the distance between
    peaks is iteratively examined and only if fewer than 30 peaks are found does the function proceed.

    :param data: np.ndarray, the sequential intensity values of the retrieved IR data
    :param range_min: int, the minimum value of the IR spectrum range in wavenumbers (typically 500 - 850)
    :param range_max:  int, the maximum value of the IR spectrum range in wavenumbers (typically 3500 - 4000)

    :return: numpy.ndarray, the rebased peak locations in wavenumbers
    """
    minimum_permitted_peaks = 30

    for i in range(1,len(data), 10):  # as an element per pixel this is a huge range, step count 10 to reduce time
        peak_locations = find_peaks(data, distance=i)[0]  # not interested in peak properties so only need locations

        if len(peak_locations) <= minimum_permitted_peaks:
            relative_peaks_percent = peak_locations[::-1] / len(data)  # image is upside down so need to invert range
            wavenumbers_range = range_max - range_min
            rebased_peak_locations = range_min + (relative_peaks_percent * wavenumbers_range)  # calculate wavenumbers
            return rebased_peak_locations


########################################################################################################################

ir_data = spectrum_image_data('Test_Spectra/nt_trim.jpg')
peaks = ir_peak_locator(ir_data, 400, 4000)
print(peaks)

