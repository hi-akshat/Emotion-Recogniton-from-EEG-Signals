import os
import sys
import numpy as np
import scipy.io as sio
import more_itertools as mit


chan = ['Fp1','AF3','F3','F7','FC5','FC1','C3','T7','CP5','CP1','P3','P7','PO3','O1','Oz','Pz','Fp2','AF4','Fz','F4','F8','FC6','FC2','Cz','C4','T8','CP6','CP2','P4','P8','PO4','O2']
nLabel, nTrial, nUser, nChannel, nTime  = 4, 40, 1, 32, 8064
print ("Program started \n")
m=[]
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
		for dat in range(384,nTime):
			for ch in range(nChannel):
					m.append(str(x['data'][tr][ch][dat]))
		windows = list(mit.windowed(m, n=512, step=256))
		if(x['labels'][tr][0]<4.5):
				fout_labels0.write(str(1) + "\n");
		else:
				fout_labels0.write(str(2) + "\n");
		if(x['labels'][tr][1]<4.5):
				fout_labels1.write(str(1) + "\n");
		else:
				fout_labels1.write(str(2) + "\n");
        #Normalizing the data between [0,1]
		windows.append(tuple([x for x in range(512)]))
		for l in range(928):
			for n in range(512):
				if n==511:
					fout_data.write(str(windows[l][n]))
				else:
					fout_data.write(str(windows[l][n])+",")
			fout_data.write("\n")
		fout_data.close()
		#maximum=np.amax(array)
		#minimum=np.amin(array)
       #normalise all data in the array except the first value of each row
		array = np.genfromtxt('features_raw.csv',delimiter=',')
		maximum=array[:928, 1:].max()
		minimum=array[:928, 1:].min()
		#normalise all data in the array except the first value of each row
		a = (array[:928,:] - minimum)/(maximum - minimum)
		np.savetxt("features_raw.csv", a, delimiter=",", fmt='%s')
		os.system('python entropy1.py')
		print("user "+ str(i+1) +" trail"+ str(tr+1))

fout_labels0.close()
fout_labels1.close()
print ("\n"+"Print Successful")