from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load a JPG/JPEG image and print its shape and pixel content.

    Args:
        path: file path to a .jpg or .jpeg image

    Returns:
        numpy array of shape (H, W, 3) with RGB pixel data,
        or None on error
    """
    if not isinstance(path, str):
        print("Error: path must be a string.")
        return None
    if not path.lower().endswith((".jpg", ".jpeg")):
        print("Error: only .jpg or .jpeg files are supported.")
        return None
    try:
        img = Image.open(path)
        img_array = np.array(img)
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")
        return None
    except Exception as e:
        print(f"Error loading image: {e}")
        return None
    print(f"The shape of image is: {img_array.shape}")
    print(img_array)
    return img_array
