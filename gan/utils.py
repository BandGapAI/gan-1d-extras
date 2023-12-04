import os
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np


def load_analytical(fname, param):
    """
    Utility functions to compare with analytical implementation
    """
    if not os.path.isfile(fname):
        return None
    return loadmat(fname)[param]

