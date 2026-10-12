import unittest

import numpy as np

from src.image_utils import get_image_info


class TestImageUtils(unittest.TestCase):

    def test_get_image_info(self):
        image = np.zeros((100, 200, 3), dtype=np.uint8)

        image_info = get_image_info(image)

        self.assertEqual(image_info["width"], 200)
        self.assertEqual(image_info["height"], 100)
        self.assertEqual(image_info["channels"], 3)

    def test_grayscale_image_info(self):
        image = np.zeros((50, 80), dtype=np.uint8)

        image_info = get_image_info(image)

        self.assertEqual(image_info["width"], 80)
        self.assertEqual(image_info["height"], 50)
        self.assertEqual(image_info["channels"], 1)


if __name__ == "__main__":
    unittest.main()