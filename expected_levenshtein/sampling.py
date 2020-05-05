#!/usr/bin/env python

import numpy as np
from numba import jit


@jit(nopython=True, parallel=True)
def _lev(a, b):
    """Computes Levenshtein distance between the two
    strings a and b.

    Args:
        a (iterable): String a
        b (iterable): String b

    Returns:
        array_like: the complete distance matrix for a and b
    """
    la, lb = len(a), len(b)
    if la < lb:
        a, b = b, a
        la, lb = lb, la
    L = np.empty(shape=(la + 1, lb + 1))
    for i in range(la + 1):
        for j in range(lb + 1):
            if i == 0:
                L[i, j] = j
            elif j == 0:
                L[i, j] = i
            else:
                h, v, d = L[i - 1, j] + 1, L[i, j - 1] + 1, L[i - 1, j - 1]
                if a[i - 1] != b[j - 1]:
                    d += 1
                L[i, j] = min(d, v, h)
    return L


def _rand_seq(l, alphabet):
    """Generates a random sequence.

    Args:
        l (int): length of the sequence
        alphabet (array_like): alphabet over which the sequence is built

    Returns:
        array_like: random sequence
    """
    return np.random.choice(alphabet, l)


def _sample_rand_lev(n, reps, alphabet):
    """Samples Levenshtein distances between random sequences.
    Generates <rep> <n> x <n> matrices of the Levenshtein distance
    calculations between random sequences built over the provided
    alphabet. Returns the element wise mean over the matrices.

    Args:
        n (int): Length of the sequence
        reps (int): number of replicates
        alphabet (array_like): alphabet over which
                               the random sequences are built

    Returns:
        array_like: (n + 1)^2 matrix with the element wise means over all reps.
    """
    sample = [
        _lev(_rand_seq(n, alphabet), _rand_seq(n, alphabet))
        for _ in range(reps)]
    return np.mean(np.array(sample), axis=0)
