import numpy as np


def max_index(X):
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise ValueError("X must be a 2D numpy array")
    cord = np.unravel_index(np.argmax(X, axis=None), X.shape)
    return cord[0], cord[1]


def wallis_product(n_terms):
    pi = 1
    for i in range(1, n_terms+1):
        pi *= 4*(i**2)/(4*(i**2)-1)
    pi *= 2
    return pi
