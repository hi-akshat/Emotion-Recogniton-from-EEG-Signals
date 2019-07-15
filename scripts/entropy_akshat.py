'''

@author : AKSHAT GUPTA
@project : Emotion Recog from EEG

'''

from numba import jit
from math import factorial, log
from sklearn.neighbors import KDTree
from scipy.signal import periodogram, welch
from .utils import _embed
import csv
from collections import defaultdict
import numpy as np
from scipy.signal import *
from numpy.fft import * 
from scipy import *
from pylab import *
import pywt


#Entropy Function Definitions

def app_entropy(x, order=2, metric='chebyshev'):
    """Approximate Entropy
    Parameters
    ----------
    x : list or np.array
        One-dimensional time series of shape (n_times)
    order : int (default: 2)
        Embedding dimension.
    metric : str (default: chebyshev)
        Name of the metric function used with
        :class:`~sklearn.neighbors.KDTree`. The list of available
        metric functions is given by: ``KDTree.valid_metrics``.
    Returns
    -------
    ae : float
        Approximate Entropy.
 
    """
    phi = _app_samp_entropy(x, order=order, metric=metric, approximate=True)
    return np.subtract(phi[0], phi[1])


def sample_entropy(x, order=2, metric='chebyshev'):
    """Sample Entropy.
    Parameters
    ----------
    x : list or np.array
        One-dimensional time series of shape (n_times)
    order : int (default: 2)
        Embedding dimension.
    metric : str (default: chebyshev)
        Name of the metric function used with KDTree. The list of available
        metric functions is given by: `KDTree.valid_metrics`.
    Returns
    -------
    se : float
        Sample Entropy.

    """
    x = np.asarray(x, dtype=np.float64)
    if metric == 'chebyshev' and x.size < 5000:
        return _numba_sampen(x, mm=order, r=0.2)
    else:
        phi = _app_samp_entropy(x, order=order, metric=metric,
                                approximate=False)
 return -np.log(np.divide(phi[1], phi[0])) 



def _app_samp_entropy(x, order, metric='chebyshev', approximate=True):
    """Utility function for `app_entropy`` and `sample_entropy`.
    """
    _all_metrics = KDTree.valid_metrics
    if metric not in _all_metrics:
        raise ValueError('The given metric (%s) is not valid. The valid '
                         'metric names are: %s' % (metric, _all_metrics))
    phi = np.zeros(2)
    r = 0.2 * np.std(x, axis=-1, ddof=1)

    # compute phi(order, r)
    _emb_data1 = _embed(x, order, 1)
    if approximate:
        emb_data1 = _emb_data1
    else:
        emb_data1 = _emb_data1[:-1]
    count1 = KDTree(emb_data1, metric=metric).query_radius(emb_data1, r,
                                                           count_only=True
                                                           ).astype(np.float64)
    # compute phi(order + 1, r)
    emb_data2 = _embed(x, order + 1, 1)
    count2 = KDTree(emb_data2, metric=metric).query_radius(emb_data2, r,
                                                           count_only=True
                                                           ).astype(np.float64)
    if approximate:
        phi[0] = np.mean(np.log(count1 / emb_data1.shape[0]))
        phi[1] = np.mean(np.log(count2 / emb_data2.shape[0]))
    else:
        phi[0] = np.mean((count1 - 1) / (emb_data1.shape[0] - 1))
        phi[1] = np.mean((count2 - 1) / (emb_data2.shape[0] - 1))
    return phi


#The main code 

fout_data = open("train.csv",'a')
vec = []
chan = ['Fp1','AF3','F3','F7','FC5','FC1','C3','T7','CP5','CP1','P3','P7','PO3','O1','Oz','Pz','Fp2','AF4','Fz','F4','F8','FC6','FC2','Cz','C4','T8','CP6','CP2','P4','P8','PO4','O2']
columns = defaultdict(list) # each value in each column is appended to a list

with open("features_raw.csv") as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k
for i in chan:
	x = np.array(columns[i]).astype(np.float)
	coeffs = pywt.wavedec(x, 'db4',level=3)
	#cD5,cD4,cD3,cD2,cD1 = coeffs
	cD4,cD3,cD2,cD1 = coeffs
	#cD5 = np.std(cD5)
	cD4 = app_entropy(cD4, order=2, metric='chebyshev')
	cD3 = app_entropy(cD3, order=2, metric='chebyshev')
	cD2 = app_entropy(cD2, order=2, metric='chebyshev')
	cD1 = app_entropy(cD1, order=2, metric='chebyshev')
	if i =="O2":
		#fout_data.write(str(cD5)+",")
		fout_data.write(str(cD4)+",")
		fout_data.write(str(cD3)+",")
		fout_data.write(str(cD2)+",")
		fout_data.write(str(cD1))
	else:
		#fout_data.write(str(cD5)+",")
		fout_data.write(str(cD4)+",")
		fout_data.write(str(cD3)+",")
		fout_data.write(str(cD2)+",")
		fout_data.write(str(cD1)+",")
fout_data.write("\n")
fout_data.close()
