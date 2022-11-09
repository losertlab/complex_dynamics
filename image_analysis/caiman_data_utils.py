import pandas as pd
import numpy as np
from statistics import mean

class CaimanDataUtils:
    def __init__(self, data):
        estimates = data['estimates']
        params = data['params']
        spatial_components = estimates['A']
        indices = spatial_components['indices']
        indptr = spatial_components['indptr']
        shape = spatial_components['shape']
        dims = params['data/dims']
        spatial_components = pd.DataFrame(np.vstack((indices[:]//dims[0], indices[:]%dims[0])).T, columns = ['x','y'])
        spatial_components['y'] = spatial_components['y'].apply(lambda x: dims[1]-x)
        
        self.dims = dims
        self.indptr = indptr
        self.spatial_components = spatial_components
        self.traces = pd.DataFrame(np.transpose(estimates['F_dff']))

    def get_spatial_component(self, idx):
        return self.spatial_components.iloc[self.indptr[idx]:self.indptr[idx+1],:]

    def get_spatial_separation(self, idx1, idx2):
        return 1
