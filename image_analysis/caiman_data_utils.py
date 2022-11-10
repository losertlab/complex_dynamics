import pandas as pd
import numpy as np
from statistics import mean
from math import sqrt
from image_analysis import correlation_matrix

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
        traces = pd.DataFrame(np.transpose(estimates['F_dff']))
        separations = np.zeros((indptr.len()-1, indptr.len()-1))
        self.dims = dims
        self.indptr = indptr
        self.spatial_components = spatial_components
        self.traces = traces
        self.corrs = correlation_matrix(traces)
        for (x, y), el in np.ndenumerate(separations):
            separations[x][y] = self.get_spatial_separation(x, y)
        self.separations = pd.DataFrame(separations)

    def get_spatial_component(self, idx):
        return self.spatial_components.iloc[self.indptr[idx]:self.indptr[idx+1],:]

    def get_spatial_separation(self, idx1, idx2):
        loc1 = self.get_spatial_component(idx1)
        loc2 = self.get_spatial_component(idx2)
        xsep = mean(loc1['x']) - mean(loc2['x'])
        ysep = mean(loc1['y']) - mean(loc2['y'])
        return sqrt(xsep**2 + ysep**2)

    def  get_pairwise_comparisons(self):
        comp = pd.DataFrame(np.repeat(np.arange(0,self.indptr.len()-1,1),self.indptr.len()), columns=['cell1'])
        comp['cell2'] = np.tile(np.arange(0,self.indptr.len()-1,1),self.indptr.len()).tolist()
        comp['corr'] = comp.apply(lambda row: self.corrs[row['cell1']][row['cell2']], axis=1)
        comp['distance'] = comp.apply(lambda row: self.separations[row['cell1']][row['cell2']], axis=1)
        
        return comp
        
