import cv2


def load_image(image_path):
    """Load an image from the specified path."""
    image = cv2.imread(str(image_path))

    if image is None:
        raise FileNotFoundError(
            f"Could not load image: {image_path}"
        )

    return image


def get_image_info(image):
    """Return the dimensions and channel count of an image."""
    height, width = image.shape[:2]
    channels = 1 if image.ndim == 2 else image.shape[2]

    return {
        "width": width,
        "height": height,
        "channels": channels,
    }