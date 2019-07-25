import numpy as np 
import pywt
import pandas as pd

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
i=0
data1=pd.read_csv("features_raw.csv",index_col=None,header=None)
for i in range(928):
	row=data1.iloc[i,:]   #selecting each row for applying dwt
	#print(row)
	coeffs=pywt.wavedec(row,'db4',level=4) #applying dwt of level 4 and wavelet family 'db4'
	cA,cB,cC,cD,cE=coeffs
	cA_values.append(cA)
	cB_values.append(cB)
	cC_values.append(cC)
	cD_values.append(cD)
	i+=1
	if i%29==0:
		cA_Energy.append(np.sum(np.square(cA_values)))               #calculating energy and entropy of 29 windows i.e. for one video for each frquency band theta, alpha, gamma, beta and storing the values in separate files for each band 
		cB_Energy.append(np.sum(np.square(cB_values)))
		cC_Energy.append(np.sum(np.square(cC_values)))
		cD_Energy.append(np.sum(np.square(cD_values)))
		Entropy_A.append(np.sum(np.square(cA_values) * np.log(np.square(cA_values))))
		Entropy_A=[-a for a in Entropy_A]
		Entropy_B.append(np.sum(np.square(cB_values) * np.log(np.square(cB_values))))
		Entropy_B=[-b for b in Entropy_B]
		Entropy_C.append(np.sum(np.square(cC_values) * np.log(np.square(cC_values))))
		Entropy_C=[-c for c in Entropy_C]
		Entropy_D.append(np.sum(np.square(cD_values) * np.log(np.square(cD_values))))
		Entropy_D=[-d for d in Entropy_D]
		fout_data1 = open("traina.csv",'a')
		fout_data2 = open("trainb.csv",'a')
		fout_data3 = open("trainc.csv",'a')
		fout_data4 = open("traind.csv",'a')
		j=0
		fout_data1.write(str(cA_Energy[j])+",")
		fout_data1.write(str(Entropy_A[j])+",")
		fout_data2.write(str(cB_Energy[j])+",")
		fout_data2.write(str(Entropy_B[j])+",")
		fout_data3.write(str(cC_Energy[j])+",")
		fout_data3.write(str(Entropy_C[j])+",")
		fout_data4.write(str(cD_Energy[j])+",")
		fout_data4.write(str(Entropy_D[j])+",")
		j+=1
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
fout_data1.write("\n")
fout_data2.write("\n")
fout_data3.write("\n")
fout_data4.write("\n")
fout_data1.close()
fout_data2.close()
fout_data3.close()
fout_data4.close()
