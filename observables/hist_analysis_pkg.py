import numpy as np
import math

def histogram_distance(data, nbins=10, range=(0,10), edges=None, weights=None):
    """ Formats the output from histogram_data
    
    histogram_distance will output things as a hist and stdev. 
    histogram_data does all the heavy lifting. As the user can
    note, histogrma_dat outputs everything while this will 
    output only the necessary variables for the max_likelihood
    method.
    
    """
    hist, stdev, bincenters, edges, slices = histogram_data(data, nbins=nbins, range=range, edges=edges, weights=None)
    
    return hist, stdev


def histogram_data(data, nbins=10, range=(0,10), edges=None, weights=None):
    """ Histogram a 1-d Array, integral normalized

    Histogram is integral normalized. A stdev is outputted as 
    sqrt(N)/norm where N is the total counts of each bin and
    norm is the normalization factor the whole histogram is
    divided by.
    
    Must specify range and number of bins
    Or a list of edges to histogram inside
    
    Weights is optional and is assumed equal weighting if None
    
    """
    
    if weights == None:
        weights = np.ones(np.shape(data)[0])
    
    if edges == None:
        hist, edges, slices = stats.binned_statistic(x, weights, statistic="sum", range=[range], bins=nbins)
    else:
        hist, edges, slices = stats.binned_statistic(x, weights, statistic="sum", edges=edges)

    normalization = math.abs(integrate_simple(hist, edges))
    
    stdev = np.sqrt(hist) / normalization
    hist = hist / normalization
    bincenters = 0.5*(edges[1:] + edges[:-1])
    
    return hist, stdev, bincenters, edges, slices
    
def integrate_simple(hist, edges):
    sum = 0.0
    for i, val in enumerate(hist):
        sum += val*(edges[i+1] - edges[i])
    
    return sum
    
    
    
    