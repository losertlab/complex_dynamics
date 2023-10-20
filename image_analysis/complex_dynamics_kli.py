from caiman_data_utils import CaimanDataUtils
import h5py
import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
from tifffile import imsave


PATH = "/Users/qianmin/research/data/locate_centroids.hdf5"
FILE = h5py.File(PATH, 'r+')

# creates 1 matrix (ie img for 1 neuron)
def binarized_matrix_help(data, xdim, ydim):
    fov = np.zeros((ydim, xdim)) # empty (black) matrix of the dim of the img

    for i in range(0, data.shape[0]): # fill in neurons
        tmp = data.iloc[i]
        fov[tmp['y'], tmp['x']] = 1 
    
    return fov

def binarized_matrix(file, xdim, ydim):
    data_obj = CaimanDataUtils(file) # caiman object
    r = np.empty([data_obj.num_cells, ydim, xdim]) 
    
    for i in range(data_obj.num_cells): # appends binarized matrix for the i'th neuron
        r[i] = binarized_matrix_help(data_obj.get_spatial_component(i), ydim, xdim)
    
    return r

def combine_matrices(a, b, c):
    combined = np.zeros((a.shape[0], a.shape[1]))
    for row in range(a.shape[0]):
        for col in range(a.shape[1]):
            if a[row, col] == 1 or b[row, col] == 1 or c[row, col] == 1:
                combined[row, col] = 1
    return combined


# dummy matrices (to test binary -> tiff on nikon)
def fake_binarized_matrix(xdim, ydim, idx):
    r = np.zeros((ydim, xdim))

    # white rectangle
    for row in range(ydim):
        for col in range(xdim):
            if ydim < idx + 100 and ydim > idx - 100:
                r[row, col] = 1

    return r

def plot_matrix(matrix, title):
    plt.imshow(matrix, cmap="gray")
    plt.title(title)
    plt.show()

def plot_binarized_matrices(data, a, b, c, d):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.tight_layout()
    
    ax1.set_title("neuron # " + str(a))
    ax1.imshow(data[a], cmap="gray")
    ax1.xlim = (0, 2048)
    ax1.ylim = (0, 2048)

    ax2.set_title("neuron # " + str(b))
    ax2.imshow(data[b], cmap="gray")
    ax2.xlim = (0, 2048)
    ax2.ylim = (0, 2048)

    ax3.set_title("neuron # " + str(c))
    ax3.imshow(data[c], cmap="gray")
    ax3.xlim = (0, 2048)
    ax3.ylim = (0, 2048)

    ax4.set_title("neuron # " + str(d))
    ax4.imshow(data[d], cmap="gray")
    ax4.xlim = (0, 2048)
    ax4.ylim = (0, 2048)

    plt.show()

# DRIVER CODE for testing if jobs can read binary tiff 
mask1 = fake_binarized_matrix(2048, 2048, 500)