from caiman_data_utils import CaimanDataUtils
import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


PATH = "/Users/qianmin/research/data/locate_centroids.hdf5"
FILE = h5py.File(PATH, 'r+')

# creates 1 matrix (ie img for 1 neuron)
def binarized_matrix_help(data):
    fov = np.zeros((2048, 2048)) # empty (black) matrix of the dim of the img

    for i in range(0, data.shape[0]): # fill in neurons
        tmp = data.iloc[i]
        fov[tmp['y'], tmp['x']] = 1 
    
    return fov

def binarized_matrix(file):
    data_obj = CaimanDataUtils(file) # caiman object
    r = np.empty([data_obj.num_cells, 2048, 2048]) 
    
    for i in range(data_obj.num_cells): # appends binarized matrix for the i'th neuron
        r[i] = binarized_matrix_help(data_obj.get_spatial_component(i))
    
    return r

def plot_binarized_matrix(data, a, b, c, d):
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

bin_mat = binarized_matrix(FILE)
plot_binarized_matrix(bin_mat, 0, 100, 200, 270)