import subprocess
import os
import h5py
import pickle

def locate_centroids(fnames, complex_dynamics_path, params, hdf5_file, cn_file):
    params = {
        "fnames": fnames,
        "fr": 4,
        "decay_time": 0.4,
        "strides": (48,48),
        "overlaps": (24,24),
        "max_shifts": (6,6),
        "max_deviation_rigid": 3,
        "pw_rigid": False,
        "p": 1,
        "nb": 3,
        "merge_thr": 0.85,
        "rf": 80,
        "stride": 20,
        "K": 4,
        "gSig": [12,12],
        "method_init": 'greedy_roi',
        "rolling_sum": True,
        "only_init": True,
        "ssub": 1,
        "tsub": 1,
        "min_SNR": 2.0,
        "rval_thr": 0.85,
        "use_cnn": True,
        "min_cnn_thr": 0.99,
        "cnn_lowest": 0.1,
        **params
    }

    """[INCOMPLETE] Locate centroids on mapping from R2 -> R1.

    Parameters:
    param1 (int): Description of the first parameter.
    param2 (int): Description of the second parameter.

    Returns:
    List[List[int]]: Description of returned value.
    """ 
    os.chdir(complex_dynamics_path+"/image_analysis")
    with open(hdf5_file, 'w') as fp:
        pass
    with open(cn_file, 'wb') as fp:
        pickle.dump([], fp)
    print('locate_centroids', flush=True)
    try:
        print(os.environ['CONDA_DEFAULT_ENV'], flush=True)
        script = ['python', 'locate_centroids_local.py', fnames, str(params), hdf5_file, cn_file]
        print(script, flush=True)
        result = subprocess.run(script, text=True, capture_output=True, check=False, shell=True)
        print(result.stdout, flush=True)
        print(result.stderr, flush=True)

    except Exception as e:
        print(e, flush=True)

    infile = open(cn_file, 'rb')
    cn = pickle.load(infile)
    infile.close()
    return h5py.File(hdf5_file, 'r+'), cn

