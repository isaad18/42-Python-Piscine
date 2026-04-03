import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(img: np.ndarray) -> np.ndarray:
    """
    Crop the center 400x400 region and keep only one channel.

    Args:
        img: numpy array of shape (H, W, C) representing the image

    Returns:
        numpy array of shape (400, 400, 1), or None on error
    """
    if not isinstance(img, np.ndarray) or img.ndim != 3:
        print("Error: img must be a 3D numpy array.")
        return None
    height, width, _ = img.shape
    if height < 400 or width < 400:
        print("Error: image is too small to crop a 400x400 region.")
        return None
    row_start = np.floor((height - 400) // 3.75).astype(int)
    col_start = np.floor((width - 400) // 1.4).astype(int)
    return img[row_start:row_start + 400, col_start:col_start + 400, :1]


def main():
    """Load animal image, zoom into the center, and display result."""
    image = ft_load("./animal.jpg")
    if image is None:
        return
    zoomed = zoom_image(image)
    if zoomed is None:
        return
    print(f"New shape after slicing: {zoomed.shape} or {zoomed.shape[:-1]}")
    print(zoomed)
    plt.imshow(zoomed, cmap='gray')
    plt.savefig('output.png')
    plt.show()


if __name__ == "__main__":
    main()
