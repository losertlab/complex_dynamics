import cv2
import glob
import logging
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import ast
import pickle

try:
    cv2.setNumThreads(0)
except:
    pass

import caiman as cm
from caiman.motion_correction import MotionCorrect
from caiman.source_extraction.cnmf import cnmf as cnmf
from caiman.source_extraction.cnmf import params as params
from caiman.utils.utils import download_demo
from caiman.summary_images import local_correlations_movie_offline

def main():
    print('locate_centroids_local', flush=True)
    for arg in sys.argv:
        print(arg, flush=True)
    pass
    cwd = os.getcwd().replace("C:", "/c").replace("\\", "/")
    fnames = [os.path.relpath(sys.argv[1], cwd)]
    opts_dict = ast.literal_eval(sys.argv[2])
    opts_dict["fnames"] = fnames 
    hdf5_file = sys.argv[3]
    cn_file = sys.argv[4]
    
    opts = params.CNMFParams(params_dict=opts_dict)
    
    if 'dview' in locals():
        cm.stop_server(dview=dview)
    c, dview, n_processes = cm.cluster.setup_cluster(
        backend='local', n_processes=None, single_thread=False)
    
    #Yr, dims, T = cm.load_memmap(fname_new)
    #images = np.reshape(Yr.T, [T] + list(dims), order='F')

    #cm.stop_server(dview=dview)

    cnm = cnmf.CNMF(n_processes, params=opts, dview=dview)
    cnm = cnm.fit_file()
    
    Yr, dims, T = cm.load_memmap(cnm.mmap_file)
    images = np.reshape(Yr.T, [T] + list(dims), order='F')
    
    Cn = cm.local_correlations(images.transpose(1,2,0))
    Cn[np.isnan(Cn)] = 0

    cnm2 = cnm.refit(images, dview=dview)

    cnm2.estimates.evaluate_components(images, cnm2.params, dview=dview)

    cnm2.estimates.detrend_df_f(quantileMin=8, frames_window=250)

    cnm2.estimates.select_components(use_object=True)

    cnm2.save(hdf5_file)
    outfile = open(cn_file, 'wb')
    pickle.dump(Cn, outfile)
    outfile.close()

    cm.stop_server(dview=dview)

if __name__ == "__main__":
    main()
