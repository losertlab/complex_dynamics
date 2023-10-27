from .caiman_data_utils import CaimanDataUtils
import h5py
import numpy as np
import matplotlib.pyplot as plt
from tifffile import imsave

# PATH = "insert/path/here"
#FILE = h5py.File(PATH, 'r+')

# mask for a single cell
def binarize_help(data, xdim, ydim):
    r = np.zeros([xdim, ydim])
    for i in range(data.shape[0]):
        tmp = data.iloc[i]
        r[tmp['y'], tmp['x']] = 1
    return r

# masks for all cells
def binarize(file, xdim, ydim):
    data_obj = CaimanDataUtils(file)
    r = np.empty([data_obj.num_cells, ydim, xdim])
    for i in range(data_obj.num_cells):
        r[i] = binarize_help(data_obj.get_spatial_component(i), ydim, xdim)
    return r

# mask that combines multiple cells
def combine(lst):
    ydim = lst[0].shape[0]
    xdim = lst[0].shape[1]
    r = np.zeros((ydim, xdim))
    for row in range(ydim):
        for col in range (xdim):
            for i in range(len(lst)):
                ans |= lst[i, row, col]
            if ans:
                r[row, col] = 1
    return r

### TESTING STUFF ###

# dummy matrix
def fake_binarize(xdim, ydim, idx):
    r = np.zeros((ydim, xdim))
    width = idx // 10
    for row in range(ydim // 2 - width // 2, ydim // 2 + width // 2):
        for col in range(idx, idx + width):
            r[row, col] = 1
    return r

