import numpy as np

def zero_pad_image(img, pad_width):
    """
    Add zero padding around a grayscale image.
    
    Args:
        img: 2D list or numpy array of pixel values
        pad_width: integer number of pixels to pad on each side
    
    Returns:
        Padded image as 2D list with integer values,
        or -1 if input is invalid
    """

    img = np.array(img)

    if img.ndim != 2 or img.size == 0:
        return -1

    if not isinstance(pad_width, int) or pad_width < 0:
        return -1

    height, width = img.shape

    new_height = height + 2 * pad_width
    new_width = width + 2 * pad_width

    padded = np.zeros((new_height, new_width))

    padded[
        pad_width:height + pad_width,
        pad_width:width + pad_width
    ] = img

    return padded.tolist()