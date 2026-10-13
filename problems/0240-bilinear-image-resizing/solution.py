import numpy as np
import math

def bilinear_resize(image, new_height: int, new_width: int) -> list:
    """
    Resize an image using bilinear interpolation.
    
    Args:
        image: 2D (grayscale) or 3D (RGB) array representing an image
        new_height: Target height of the resized image
        new_width: Target width of the resized image
    
    Returns:
        Resized image as a nested list with values rounded to 2 decimal places
    """
    img = np.array(image)
    is_3d = img.ndim == 3
    
    old_height, old_width = img.shape[0], img.shape[1]

    s_y = old_height / new_height
    s_x = old_width / new_width

    resized = []

    for i in range(new_height):
        row = []
        for j in range(new_width):

            y = i * s_y
            x = j * s_x

            y0 = int(math.floor(y))
            x0 = int(math.floor(x))
            y1 = y0 + 1
            x1 = x0 + 1

            y0 = min(y0, old_height - 1)
            x0 = min(x0, old_width - 1)
            y1 = min(y1, old_height - 1)
            x1 = min(x1, old_width - 1)

            dy = y - y0
            dx = x - x0

            if is_3d:
                pixel = []
                for c in range(img.shape[2]):
                    val = (img[y0, x0, c] * (1 - dx) * (1 - dy) +
                           img[y0, x1, c] * dx * (1 - dy) +
                           img[y1, x0, c] * (1 - dx) * dy +
                           img[y1, x1, c] * dx * dy)
                    pixel.append(round(float(val), 2))
                row.append(pixel)
            else:
                val = (img[y0, x0] * (1 - dx) * (1 - dy) +
                       img[y0, x1] * dx * (1 - dy) +
                       img[y1, x0] * (1 - dx) * dy +
                       img[y1, x1] * dx * dy)
                row.append(round(float(val), 2))
                
        resized.append(row)

    return resized