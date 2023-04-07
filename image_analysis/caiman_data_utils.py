import pandas as pd
import numpy as np
from statistics import mean
from math import sqrt
from image_analysis import correlation_matrix
import bokeh.plotting as bpl

class CaimanDataUtils:
    def __init__(self, data):
        estimates = data['estimates']
        params = data['params']
        spatial_components = estimates['A']
        indices = spatial_components['indices']
        indptr = spatial_components['indptr']
        shape = spatial_components['shape']
        dims = params['data/dims']
        spikes = estimates.S
        traces = None
        corrs = None
        spatial_components = pd.DataFrame(np.vstack((indices[:]//dims[0], indices[:]%dims[0])).T, columns = ['x','y'])
        spatial_components['idx'] = np.nan
        idx_num = 0
        for i in np.arange(indptr.len()-1):
            spatial_components['idx'] = spatial_components.idx.fillna(value=i, limit=indptr[i+1]-indptr[i])
        traces = pd.DataFrame(np.transpose(estimates['F_dff']))
        self.estimates = estimates
        self.params = params
        self.dims = dims
        self.indptr = indptr
        self.spatial_components = spatial_components
        self.traces = traces
        self.separations = None
        self.num_cells = shape[1]-1
        self.cell_locs = None
        #self.filtered_components = spatial_components

    def get_corrs(self):
        if not self.corrs:
            self.corrs = correlation_matrix(self.traces)
        return self.corrs

    def get_cell_locs(self):
        if not self.cell_locs:
            self.cell_locs = []
            for i in range(self.num_cells):
                roi = self.get_spatial_component(i)
                x = mean(roi['x'])
                y = mean(roi['y'])
                self.cell_locs.append((x,y))


    def get_spatial_component(self, idx):
        idxn = [idx] if np.isscalar(idx) else idx
        components = pd.DataFrame(columns=['idx','x','y'])
        components = pd.concat([components, self.spatial_components.loc[self.spatial_components['idx'].isin(idxn)]])
        return components

    def get_spatial_separation(self, idx1, idx2):
        loc1 = self.get_spatial_component(idx1)
        loc2 = self.get_spatial_component(idx2)
        xsep = mean(loc1['x']) - mean(loc2['x'])
        ysep = mean(loc1['y']) - mean(loc2['y'])
        return sqrt(xsep**2 + ysep**2)

    def  get_pairwise_comparisons(self):
        if not self.separations:
            separations = np.zeros((indptr.len()-1, indptr.len()-1))
            for (x, y), el in np.ndenumerate(separations):
                separations[x][y] = self.get_spatial_separation(x, y)
            self.separations = pd.DataFrame(separations)
        
        comp = pd.DataFrame(np.repeat(np.arange(0,self.indptr.len()-1,1),self.indptr.len()), columns=['cell1'])
        comp['cell2'] = np.tile(np.arange(0,self.indptr.len()-1,1),self.indptr.len()).tolist()
        comp['corr'] = comp.apply(lambda row: self.corrs[row['cell1']][row['cell2']], axis=1)
        comp['distance'] = comp.apply(lambda row: self.separations[row['cell1']][row['cell2']], axis=1)
        
        return comp
    
    def get_image_overlay(self, title="title"):
        graph = bpl.figure(title=title)
        graph.scatter(self.spatial_components['x'], self.spatial_components['y'])
        return graph

    def filter_boundary(self):
        x = self.spatial_components['x']
        y = self.spatial_components['y']
        self.filtered_components = self.spatial_components.loc[~((self.spatial_components['x']+1).isin(x) & self.spatial_components['y'].isin(y)) | ~((self.spatial_components['x']-1).isin(x) & self.spatial_components['y'].isin(y)) | ~((self.spatial_components['y']+1).isin(y) & self.spatial_components['x'].isin(x)) | ~((self.spatial_components['y']-1).isin(y) & self.spatial_components['x'].isin(x))]
       
    corrs = property(get_corrs)


