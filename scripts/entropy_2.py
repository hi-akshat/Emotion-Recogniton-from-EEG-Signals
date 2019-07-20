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
cE_values = []
cB_values = []
cC_values = []
cD_values = []
cE_Energy =[]
cB_Energy =[]
cC_Energy =[]
cD_Energy = []
Entropy_E = []
Entropy_B = []
Entropy_C = []
Entropy_D = []
i=0
data1=pd.read_csv("features_raw.csv")
for index, row in data1.iterrows():
	coeffs=pywt.wavedec(row,'db4',level=4)
	cA,cB,cC,cD,cE=coeffs
	cE_values.append(cE)
	cB_values.append(cB)
	cC_values.append(cC)
	cD_values.append(cD)
	i+=1
	if i%29==0:
		'''cB_Energy.append(np.sum(np.square(cB_values)))
		cC_Energy.append(np.sum(np.square(cC_values)))
		cD_Energy.append(np.sum(np.square(cD_values)))
		cE_Energy.append(np.sum(np.square(cE_values)))
		Entropy_B.append(np.sum(np.square(cB_values) * np.log(np.square(cB_values))))
		Entropy_B=[-a for a in Entropy_B]
		Entropy_C.append(np.sum(np.square(cC_values) * np.log(np.square(cC_values))))
		Entropy_C=[-b for b in Entropy_C]
		Entropy_D.append(np.sum(np.square(cD_values) * np.log(np.square(cD_values))))
		Entropy_D=[-c for c in Entropy_D]
		Entropy_E.append(np.sum(np.square(cE_values) * np.log(np.square(cE_values))))
		Entropy_E=[-d for d in Entropy_E]'''
		fout_data1 = open("trainb.csv",'a')
		fout_data2 = open("trainc.csv",'a')
		fout_data3 = open("traind.csv",'a')
		fout_data4 = open("traine.csv",'a')
		fout_data1.write(str(cB_values)+",")
		fout_data2.write(str(cC_values)+",")
		fout_data3.write(str(cD_values)+",")
		fout_data4.write(str(cE_values)+",")
		'''fout_data1.write(str(cB_Energy[0])+",")
		fout_data1.write(str(Entropy_B[0])+"\n")
		fout_data2.write(str(cC_Energy[0])+",")
		fout_data2.write(str(Entropy_C[0])+"\n")
		fout_data3.write(str(cD_Energy[0])+",")
		fout_data3.write(str(Entropy_D[0])+"\n")
		fout_data4.write(str(cE_Energy[0])+",")
		fout_data4.write(str(Entropy_E[0])+"\n")'''
		fout_data1.close()
		fout_data2.close()
		fout_data3.close()
		fout_data4.close()
		cE_values = []
		cB_values = []
		cC_values = []
		cD_values = []
		cE_Energy =[]
		cB_Energy =[]
		cC_Energy =[]
		cD_Energy = []
		Entropy_E = []
		Entropy_B = []
		Entropy_C = []
		Entropy_D = []
