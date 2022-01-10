import numpy as np


def max_index(X):
    i = 0
    j = 0

    if type(X) != np.ndarray:
        raise ValueError
    if len(X.shape) != 2:
        raise ValueError

    ii = 0
    while ii < len(X):
        jj = 0
        while jj < len(X[0]):
            if X[ii][jj] > X[i][j]:
                j = jj
                i = ii
            jj = jj+1
        ii = ii+1

    return i, j


def wallis_product(n_terms):

    if type(n_terms) != int:
        raise ValueError

    if n_terms < 0:
        raise ValueError
    if n_terms == 0:
        return(2)

    i = 1
    p = 1
    while i < n_terms+1:
        p = p * (4*i**2)/(4*i**2-1)
        i = i+1
    return(2*p)
