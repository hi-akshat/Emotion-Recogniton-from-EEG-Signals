from math import factorial, log
from sklearn.neighbors import KDTree
import csv
from collections import defaultdict
import numpy as np 
from scipy import *
from pylab import *
import pywt
import pandas as pd

chan = ['Fp1','AF3','F3','F7','FC5','FC1','C3','T7','CP5','CP1','P3','P7','PO3','O1','Oz','Pz','Fp2','AF4','Fz','F4','F8','FC6','FC2','Cz','C4','T8','CP6','CP2','P4','P8','PO4','O2']

reader=np.genfromtxt("features_raw.csv",delimiter=",")
#wavelet_features(reader)

cA_values = []
cB_values = []
cC_values = []
cD_values = []
cA_Energy =[]
cB_Energy =[]
cC_Energy =[]
cD_Energy = []
Entropy_A = []
Entropy_B = []
Entropy_C = []
Entropy_D = []

ca_data = open("cA_values.csv",'w')
cb_data = open("cB_values.csv",'w')
cc_data = open("cC_values.csv",'w')
cd_data = open("cD_values.csv",'w')

for i in range(928):
    coeffs=pywt.wavedec(reader[i],'db4',level=3)
    cA,cB,cC,cD=coeffs
    #calculating the coefficients of wavelet transform.   
    ca_data.write(str(cA))
    ca_data.write("\n")    
    cb_data.write(str(cB))
    cb_data.write("\n")
    cc_data.write(str(cC))
    cc_data.write("\n")
    cd_data.write(str(cD))
    cd_data.write("\n")
    
    
    

'''for x in range(928):
    cA_Energy.append(np.sum(np.square(cA_values[x])))
    cB_Energy.append(np.sum(np.square(cB_values[x])))
    cC_Energy.append(np.sum(np.square(cC_values[x])))
    cD_Energy.append(np.sum(np.square(cD_values[x])))
    Entropy_A.append(np.sum(np.square(cA_values[x]) * np.log(np.square(cA_values[x]))))
    Entropy_A=[-a for a in Entropy_A]
    Entropy_B.append(np.sum(np.square(cB_values[x]) * np.log(np.square(cB_values[x]))))
    Entropy_B=[-b for b in Entropy_B]
    Entropy_C.append(np.sum(np.square(cC_values[x]) * np.log(np.square(cC_values[x]))))
    Entropy_C=[-c for c in Entropy_C]
    Entropy_D.append(np.sum(np.square(cD_values[x]) * np.log(np.square(cD_values[x]))))
    Entropy_D=[-d for d in Entropy_D]'''

fout_data = open("train.csv",'a')

#fout_data2 = open("trainb.csv",'a')
#fout_data3 = open("trainc.csv",'a')
#fout_data4 = open("traind.csv",'a')

for j in range(512):
    if j =="O2":
        fout_data.write(str(cA_Energy[j])+",")
        fout_data.write(str(Entropy_A[j])+",")
        fout_data.write(str(cB_Energy[j])+",")
        fout_data.write(str(Entropy_B[j])+",")
        fout_data.write(str(cC_Energy[j])+",")
        fout_data.write(str(Entropy_C[j])+",")
        fout_data.write(str(cD_Energy[j])+",")
        fout_data.write(str(Entropy_D[j]))

    else:
        fout_data.write(str(cA_Energy[j])+",")
        fout_data.write(str(Entropy_A[j])+",")
        fout_data.write(str(cB_Energy[j])+",")
        fout_data.write(str(Entropy_B[j])+",")
        fout_data.write(str(cC_Energy[j])+",")
        fout_data.write(str(Entropy_C[j])+",")
        fout_data.write(str(cD_Energy[j])+",")
        fout_data.write(str(Entropy_D[j])+",")

fout_data.write("\n")
#fout_data2.write("\n")
#fout_data3.write("\n")
#fout_data4.write("\n")

fout_data.close()
#fout_data2.close()
#fout_data3.close()
#fout_data4.close()