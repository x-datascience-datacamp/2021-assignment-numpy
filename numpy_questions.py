"""Assignment - using numpy and making a PR.

The goals of this assignment are:
    * Use numpy in practice with two easy exercises.
    * Use automated tools to validate the code (`pytest` and `flake8`)
    * Submit a Pull-Request on github to practice `git`.
The two functions below are skeleton functions. The docstrings explain what
are the inputs, the outputs and the expected error. Fill the function to
complete the assignment. The code should be able to pass the test that we
wrote. To run the tests, use `pytest test_numpy_question.py` at the root of
the repo. It should say that 2 tests ran with success.
We also ask to respect the pep8 convention: https://pep8.org.
This will be enforced with `flake8`. You can check that there is no flake8
errors by calling `flake8` at the root of the repo.
"""
import numpy as np


def max_index(X):
    """Return the index of the maximum in a numpy array.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        The input array.
    Returns
    -------
    (i, j) : tuple(int)
        The row and columnd index of the maximum.
    Raises
    ------
    ValueError
        If the input is not a numpy array or
        if the shape is not 2D.
    """
    i = 0
    j = 0

    # test argument d'appel de la fonction
    deb_msg = "ERROR max_index:"
    fin_msg = " passed in argument)"

    type_of_X = type(X)
    if not isinstance(X, np.ndarray):
        message_Erreur = \
            "{} X must be an Numpy array ({}{}" \
            .format(deb_msg, type_of_X, fin_msg)
        raise ValueError(message_Erreur)

    dim_of_X = len(X.shape)
    if dim_of_X != 2:
        message_Erreur = \
            "{} the shape of X must be 2D ({}D{}" \
            .format(deb_msg, dim_of_X, fin_msg)
        raise ValueError(message_Erreur)

    i, j = np.unravel_index(X.argmax(), X.shape)

    return i, j


def wallis_product(n_terms):
    """Implement the Wallis product to compute an approximation of pi.

    See:
    https://en.wikipedia.org/wiki/Wallis_product
    Parameters
    ----------
    n_terms : int
        Number of steps in the Wallis product. Note that `n_terms=0` will
        consider the product to be `1`.
    Returns
    -------
    pi : float
        The approximation of order `n_terms` of pi using the Wallis product.
    """
    if n_terms < 0:
        deb_msg = "ERROR wallis_product:"
        fin_msg = " passed in argument)"
        message_Erreur = \
            "{} n_terms must be positive or null (value {}{}" \
            .format(deb_msg, n_terms, fin_msg)
        raise ValueError(message_Erreur)
    else:
        pi = 1
        for i in range(1, n_terms+1):
            num = 4 * i**2
            pi *= num / (num - 1)

        pi *= 2

    return pi
