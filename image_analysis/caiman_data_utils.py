import pandas as pd
import numpy as np

class CaimanDataUtils:
    def __init__(self, data):
        estimates = data['estimates']
        params = data['params']
        spatial_components = estimates['A']
        indices = spatial_components['indices']
        indptr = spatial_components['indptr']
        shape = spatial_components['shape']
        dims = params['data/dims']
        pos = pd.DataFrame(np.vstack((indices[:]//dims[0], indices[:]%dims[0])).T, columns = ['x','y'])
        
        self.dims = dims
        self.pos = pos
        self.traces = pd.DataFrame(np.transpose(estimates['F_dff']))
