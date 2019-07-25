import os
import numpy as np
import scipy.io as sio
import more_itertools as mit
import csv
chan = ['Fp1','AF3','F3','F7','FC5','FC1','C3','T7','CP5','CP1','P3','P7','PO3','O1','Oz','Pz','Fp2','AF4','Fz','F4','F8','FC6','FC2','Cz','C4','T8','CP6','CP2','P4','P8','PO4','O2']
nLabel, nTrial, nUser, nChannel, nTime  = 4, 40, 32, 32, 8064 #nTrial stands for the no. of videos, nUser stands for the no. of users, nTime stands for the data (8064)
print ("Program started \n")
m=[]
windows=[]
fout_labels0 = open("labels_0.dat",'w')
fout_labels1 = open("labels_1.dat",'w')
for i in range(nUser):#4, 40, 32, 32, 8064
	if i < 10:
		name = '%0*d' % (2,i+1)
	else:
		name = i+1
	fname = "s"+str(name)+".mat"
	x = sio.loadmat(fname)
	print (fname)
	for tr in range(nTrial):
		fout_data = open("features_raw.csv",'w')
		for ch in range(nChannel):
			for dat in range(384,nTime):  #excluding data for first 3 seconds as 8064 data items are for 63 seconds and the first 3 seconds are just to reduce the discripency
				if ch <32:
					if dat==nTime:
						fout_data.write(str(x['data'][tr][ch[dat]]))
					else:
						fout_data.write(str(x['data'][tr][ch][dat])+",");#each row is a channel i.e. why here we're having 7680 columns and 32 rows
			fout_data.write("\n")
		fout_data.close();
		array =np.genfromtxt("features_raw.csv", delimiter=',')#applying the amr(average mean reference)
		sum=np.sum(array[:,:7680])
		b=array.shape
		total=b[0]*(b[1]-1)
		amr=(sum/total)
		a = (array[:,:7680] - amr)
		np.savetxt("features_raw.csv", a, delimiter=",", fmt='%s')
		array = np.genfromtxt('features_raw.csv',delimiter=',')#applying min-max normalisation and storing the array in the csv file
		for g in range(32):
			maximum=array[g, :].max()
			minimum=array[g, :].min()
			a = (array[g,:] - minimum)/(maximum - minimum)
		fout_data=open("features_raw.csv",'a')
		o=0
		for s in range(7680):
			if o==31:
				fout_data.write(str(a[s])+"\n")
			else:
				fout_data.write(str(a[s])+",")
		o+=1                
		fout_data.close()
		f=open("features_raw.csv")
		csv_f=csv.reader(f)
		for row in csv_f:        
			m.append(list(row))
			windows.append(list(mit.windowed(m[0], n=512, step=256))) # creating windows as for each second in a single channel we get 128 values and hence for a window of 4 seconds (512 values) and an overlap of 2 seconds (256 values)
			m=[]
		fout_data = open("features_raw.csv",'w')
		for l in range(32):
			for n in range(29):
				for s in range(512):
					if s==511:
						fout_data.write(str(windows[l][n][s]))
					else:
						fout_data.write(str(windows[l][n][s])+",")
				fout_data.write("\n")
		fout_data.close()
		windows=[]
		if(x['labels'][tr][0]<4.5):               #labelling the values of arousal and valence given by the users on a scale of greater than 4.5 and less than 4.5
			fout_labels0.write(str(0) + "\n");
		else:
			fout_labels0.write(str(1) + "\n");
		if(x['labels'][tr][1]<4.5):
			fout_labels1.write(str(0) + "\n");
		else:
			fout_labels1.write(str(1) + "\n");
		os.system('python feature_extraction.py')          #calling the file for calculating the dwt, energy, entropy 
		print("User "+ str(i+1) +" : Trial"+ str(tr+1) + "processed.")
fout_labels0.close()
fout_labels1.close()
print ("\n"+"Print Successful")