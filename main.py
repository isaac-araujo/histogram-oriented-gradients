import os

import cv2
import matplotlib.pyplot as plt
import numpy as np


def resize_image(image):
    # Resize
    height, width = image.shape[:2]
    new_height = height - (height % 8)
    new_width = width - (width % 8)
    return cv2.resize(image, (new_width, new_height))


def compute_gradients(image):
    dx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    dy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    # Magnitude
    magnitude = cv2.addWeighted(dx, 0.5, dy, 0.5, 0)
    # cv2.imshow("magnitude", magnitude)
    # Orientation
    orientation = np.arctan2(dy, dx)
    # cv2.imshow("orientation", orientation)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return magnitude, orientation


def compute_histogram(orientation, magnitude, num_bins=9):
    hist = np.zeros(num_bins)
    bin_width = 360 / num_bins
    orientation = orientation % 360
    for i in range(num_bins):
        hist[i] = np.sum(
            magnitude[
                np.where((orientation >= i * bin_width) & (orientation < (i + 1) * bin_width))
            ]
        )
    return hist


def compute_hog(image, cell_size=(8, 8), num_bins=9):
    image = resize_image(image)
    magnitude, orientation = compute_gradients(image)

    height, width = magnitude.shape[:2]
    # cells_per_block = (block_size[0] // cell_size[0], block_size[1] // cell_size[1])
    num_cels = (height // cell_size[0], width // cell_size[1])

    hog_image = np.zeros((height, width), dtype=float)
    for i in range(num_cels[0]):
        for j in range(num_cels[1]):
            cell_mag = magnitude[
                i * cell_size[0] : (i + 1) * cell_size[0],
                j * cell_size[1] : (j + 1) * cell_size[1]
            ]
            cell_ori = orientation[
                i * cell_size[0] : (i + 1) * cell_size[0],
                j * cell_size[1] : (j + 1) * cell_size[1],
            ]
            cell_histogram = compute_histogram(cell_ori, cell_mag, num_bins)
            hog_image[
                i * cell_size[0] : (i + 1) * cell_size[0],
                j * cell_size[1] : (j + 1) * cell_size[1]
            ] = cell_histogram[0]
    return hog_image


for name_img in os.listdir("images"):
    image = cv2.imread(f"images/{name_img}", cv2.IMREAD_GRAYSCALE)

    hog_image = compute_hog(image)

    # cv2.imwrite(f"images_hog/{name_img}", hog_image)
    plt.imshow(hog_image, cmap="gray")
    plt.axis("off")
    plt.savefig(f"images_hog/{name_img}")

    # plt.show()
