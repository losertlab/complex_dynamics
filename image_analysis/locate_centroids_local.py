import cv2
import glob
import logging
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import ast

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
    pass
    opts_dict = ast.literal_eval(sys.argv[2])
    opts_dict["fnames"] = os.path.relpath(opts_dict["fnames"], os.getcwd().replace("C:", "/c").replace("\\", "/"))
    
    print(os.path.isfile(opts_dict["fnames"]))
    #opts = params.CNMFParams(params_dict=opts_dict)

if __name__ == "__main__":
    main()
