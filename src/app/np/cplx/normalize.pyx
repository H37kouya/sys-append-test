import cython
import numpy as np
cimport numpy as np


cdef extern from "math.h":
    cdef double sqrt(double x)


ctypedef np.complex128_t DTYPE_t


@cython.boundscheck(False)
@cython.wraparound(False)
def normalize(
        np.ndarray[DTYPE_t, ndim=1] arr
) -> np.ndarray:
    """
    正規化

    :param arr:
    :return: 正規化した値
    """

    abs_arr = np.abs(arr)
    cdef double sum_of_squares = (abs_arr * abs_arr).sum()
    cdef double norm = sqrt(sum_of_squares)
    return arr / norm


@cython.boundscheck(False)
@cython.wraparound(False)
def normalize_with_norm(
        np.ndarray[DTYPE_t, ndim=1] arr
) -> tuple[np.ndarray, float]:
    """
    正規化

    :param arr:
    :return: 正規化した値とノルム
    """
    abs_arr = np.abs(arr)
    cdef double sum_of_squares = (abs_arr * abs_arr).sum()
    cdef double norm = sqrt(sum_of_squares)
    return arr / norm, norm