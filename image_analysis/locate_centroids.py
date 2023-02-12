import subprocess
import os

complex_dynamics_path = os.getcwd()

def locate_centroids(fnames, complex_dynamics_path,
        fr=3,
        decay_time=0.4,
        strides=(48,48),
        overlaps=(24,24),
        max_shifts=(6,6),
        max_deviation_rigid=3,
        pw_rigid=False,
        p=1,
        gnb=3,
        merge_thr=0.85,
        rf=80,
        stride_cnmf=20,
        K=4,
        gSig=[12,12],
        method_init='greedy_roi',
        ssub=1,
        tsub=1,
        min_SNR=2.0,
        rval_thr=0.85,
        cnn_thr=0.99,
        cnn_lowest=0.1):
    """[INCOMPLETE] Locate centroids on mapping from R2 -> R1.

    Parameters:
    param1 (int): Description of the first parameter.
    param2 (int): Description of the second parameter.

    Returns:
    List[List[int]]: Description of returned value.
    """ 
    os.chdir(complex_dynamics_path+"/image_analysis")
    #loc = {}
    #exec(open("locate_centroids_local.py").read(), globals(), loc)
    #return loc["test"]
    return subprocess.run(['python', 'locate_centroids_local.py'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')

