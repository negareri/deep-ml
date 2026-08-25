import numpy as np

def rgb_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminosity method.
    
    Args:
        image: RGB image as list or numpy array of shape (H, W, 3)
               with values in range [0, 255]
    
    Returns:
        Grayscale image as 2D list with integer values,
        or -1 if input is invalid
    """
    if not image:
        return -1

    for i in range(len(image)):
        for j in range(len(image[0])):
            if not isinstance(image[i][j], list):
                return -1
            for k in range(3):
                if image[i][j][k] < 0 or image[i][j][k] > 255:
                    return -1

    result = []
    for i in range(len(image)):
        row = []
        for j in range(len(image[0])):
            sums = image[i][j][0] * 0.299 + image[i][j][1] * 0.587 + image[i][j][2] * 0.114
            row.append(round(sums, 0))
        result.append(row)

    return result
