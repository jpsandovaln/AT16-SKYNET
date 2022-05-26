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

import math
from operator import __mul__, __add__, __getitem__, __sub__, __neg__, __pow__
from statistics import mean
from turtle import shape

import numpy as np
from numpy import ndim, ndarray, std
from skimage.util import view_as_blocks


def polar2cart(r: {__mul__}, x0: {__add__}, y0: {__add__}, theta: float) -> int:
    """Changes polar coordinates to cartesian coordinate system.

    :param r: Radius
    :param x0: x coordinate of the origin
    :param y0: y coordinate of the origin
    :param theta: Angle
    :return: Cartesian coordinates
    :rtype: tuple (int, int)
    """
    x: int = int(x0 + r * math.cos(theta))
    y: int = int(y0 + r * math.sin(theta))
    return x, y


def unravel_iris(img: {ndim, __getitem__, shape}, xp: {__add__}, yp: {__add__}, rp: {__mul__}, xi: {__add__},
                 yi: {__add__}, ri: {__mul__}, phase_width: int = 300, iris_width: int = 150) -> ndarray:
    """Unravels the iris from the image and transforms it to a straightened representation.

    :param img: Image of an eye
    :param xp: x coordinate of the pupil centre
    :param yp: y coordinate of the pupil centre
    :param rp: Radius of the pupil
    :param xi: x coordinate of the iris centre
    :param yi: y coordinate of the iris centre
    :param ri: Radius of the iris
    :param phase_width: Length of the transformed iris
    :param iris_width: Width of the transformed iris
    :return: Straightened image of the iris
    :rtype: ndarray
    """
    if img.ndim > 2:
        img: {ndim, __getitem__, shape} = img[:, :, 0].copy()
    iris: ndarray = np.zeros((iris_width, phase_width))
    theta: ndarray | tuple[ndarray, float | None] = np.linspace(0, 2 * np.pi, phase_width)
    for i in range(phase_width):
        begin: int = polar2cart(rp, xp, yp, theta[i])
        end: int = polar2cart(ri, xi, yi, theta[i])
        xspace: ndarray | tuple[ndarray, float | None] = np.linspace(begin[0], end[0], iris_width)
        yspace: ndarray | tuple[ndarray, float | None] = np.linspace(begin[1], end[1], iris_width)
        iris[:, i] = [255 - img[int(y), int(x)]
                      if 0 <= int(x) < img.shape[1] and 0 <= int(y) < img.shape[0]
                      else 0
                      for x, y in zip(xspace, yspace)]
    return iris


def gabor(rho: {__sub__}, phi: {__sub__}, w: {__neg__}, theta0: {__sub__}, r0: any, alpha: {__pow__},
          beta: {__pow__}) -> any:
    """Calculates gabor wavelet.

    :param rho: Radius of the input coordinates
    :param phi: Angle of the input coordinates
    :param w: Gabor wavelet parameter (see the formula)
    :param theta0: Gabor wavelet parameter (see the formula)
    :param r0: Gabor wavelet parameter (see the formula)
    :param alpha: Gabor wavelet parameter (see the formula)
    :param beta: Gabor wavelet parameter (see the formula)
    :return: Gabor wavelet value at (rho, phi)
    """
    return np.exp(-w * 1j * (theta0 - phi)) * np.exp(-(rho - r0) ** 2 / alpha ** 2) * \
           np.exp(-(phi - theta0) ** 2 / beta ** 2)


def gabor_convolve(img: {shape}, w: {__neg__}, alpha: {__pow__}, beta: {__pow__}) -> tuple[ndarray, ndarray]:
    """Uses gabor wavelets to extract iris features.

    :param img: Image of an iris
    :param w: w parameter of Gabor wavelets
    :param alpha: alpha parameter of Gabor wavelets
    :param beta: beta parameter of Gabor wavelets
    :return: Transformed image of the iris (real and imaginary)
    :rtype: tuple (ndarray, ndarray)
    """
    rho: any = np.array([np.linspace(0, 1, img.shape[0]) for i in range(img.shape[1])]).T
    x: ndarray | tuple[ndarray, float | None] = np.linspace(0, 1, img.shape[0])
    y: ndarray | tuple[ndarray, float | None] = np.linspace(-np.pi, np.pi, img.shape[1])
    xx, yy = np.meshgrid(x, y)
    return rho * img * np.real(gabor(xx, yy, w, 0, 0.5, alpha, beta).T), \
           rho * img * np.imag(gabor(xx, yy, w, 0, 0.5, alpha, beta).T)


def iris_encode(img: {__lt__, __sub__, mean, std}, dr: int = 15, dtheta: int = 15, alpha: float = 0.4) -> ndarray:
    """Encodes the straightened representation of an iris with gabor wavelets.

    :param img: Image of an iris
    :param dr: Width of image patches producing one feature
    :param dtheta: Length of image patches producing one feature
    :param alpha: Gabor wavelets modifier (beta parameter of Gabor wavelets becomes inverse of this number)
    :return: Iris code and its mask
    :rtype: tuple (ndarray, ndarray)
    """
    # mean = np.mean(img)
    # std = img.std()
    mask: any = view_as_blocks(np.logical_and(100 < img, img < 230), (dr, dtheta))
    norm_iris: int = (img - img.mean()) / img.std()
    patches: any = view_as_blocks(norm_iris, (dr, dtheta))
    code: ndarray = np.zeros((patches.shape[0] * 3, patches.shape[1] * 2))
    code_mask: ndarray = np.zeros((patches.shape[0] * 3, patches.shape[1] * 2))
    for i, row in enumerate(patches):
        for j, p in enumerate(row):
            for k, w in enumerate([8, 16, 32]):
                wavelet = gabor_convolve(p, w, alpha, 1 / alpha)
                code[3 * i + k, 2 * j]: ndarray = np.sum(wavelet[0])
                code[3 * i + k, 2 * j + 1]: ndarray = np.sum(wavelet[1])
                code_mask[3 * i + k, 2 * j] = code_mask[3 * i + k, 2 * j + 1] = \
                    1 if mask[i, j].sum() > dr * dtheta * 3 / 4 else 0
    code[code >= 0] = 1
    code[code < 0] = 0
    return code, code_mask
