from math import factorial, log
from sklearn.neighbors import KDTree
import csv
from collections import defaultdict
import numpy as np 
from scipy import *
from pylab import *
import pywt
import pandas as pd

vec = []
chan = ['Fp1','AF3','F3','F7','FC5','FC1','C3','T7','CP5','CP1','P3','P7','PO3','O1','Oz','Pz','Fp2','AF4','Fz','F4','F8','FC6','FC2','Cz','C4','T8','CP6','CP2','P4','P8','PO4','O2']

reader=np.genfromtxt("features_raw.csv",delimiter=",",skip_header=1)
#wavelet_features(reader)
if 1:
        cA_values = []
        cD_values = []
        cA_mean = []
        cA_std = []
        cA_Energy =[]
        cD_mean = []
        cD_std = []
        cD_Energy = []
        Entropy_D = []
        Entropy_A = []
        for i in range(32):
            cA,cD=pywt.dwt(reader[i,:],'db4')
            cA_values.append(cA)
            cD_values.append(cD)		#calculating the coefficients of wavelet transform.   
        for x in range(32):
            cA_mean.append(np.mean(cA_values[x]))
            cA_std.append(np.std(cA_values[x]))
            cA_Energy.append(np.sum(np.square(cA_values[x])))
            cD_mean.append(np.mean(cD_values[x]))		# mean and standard deviation values of coefficents of each channel is stored .
            cD_std.append(np.std(cD_values[x]))
            cD_Energy.append(np.sum(np.square(cD_values[x])))
            Entropy_D.append(np.sum(np.square(cD_values[x]) * np.log(np.square(cD_values[x]))))
            Entropy_A.append(np.sum(np.square(cA_values[x]) * np.log(np.square(cA_values[x]))))
        dict = {'cA_Energy': cA_Energy, 'cD_Energy':cD_Energy, 'Entropy_A':Entropy_A, 'Entropy_D':Entropy_D}
        df = pd.DataFrame(dict)
        with open('train.csv','a') as f:
                     df.to_csv(f, header=False,index_col=False)