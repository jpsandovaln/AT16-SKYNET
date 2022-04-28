# MIT License
#
# Copyright (c) 2017 Tomasz Danel
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from src.model.model_iris_recognition.segmentation import *
from src.model.model_iris_recognition.coding import *


class Recognition():
    def compare_codes(self, a, b, mask_a, mask_b, rotation=False):
        """Compares two codes and calculates Jaccard index.

        :param a: Code of the first iris
        :param b: Code of the second iris
        :param mask_a: Mask of the first iris
        :param mask_b: Mask of the second iris
        :param rotation: Maximum cyclic rotation of the code. If this argument is greater than zero, the function will
            return minimal distance of all code rotations. If this argument is False, no rotations are calculated.

        :return: Distance between two codes, that means if the objects are similars will be near to 0.
        """
        if rotation:
            d = []
            for i in range(-rotation, rotation + 1):
                c = np.roll(b, i, axis=1)
                mask_c = np.roll(mask_b, i, axis=1)
                d.append(
                    np.sum(np.remainder(a + c, 2) * mask_a * mask_c) / np.sum(
                        mask_a * mask_c))
            return np.min(d)
        return np.sum(np.remainder(a + b, 2) * mask_a * mask_b) / np.sum(
            mask_a * mask_b)

    def encode_photo(self, image):
        """Finds the pupil and iris of the eye, and then encodes the unravelled iris.

        :param image: Image of an eye
        :return: Encoded iris (code, mask)
        :rtype: tuple (ndarray, ndarray)
        """
        img = preprocess(image)
        x, y, r = find_pupil_hough(img)
        x_iris, y_iris, r_iris = find_iris_id(img, x, y, r)
        iris = unravel_iris(image, x, y, r, x_iris, y_iris, r_iris)
        return iris_encode(iris)


