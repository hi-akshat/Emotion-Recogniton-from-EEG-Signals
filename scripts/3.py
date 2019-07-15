from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import KFold,train_test_split
def get_score(model,X_train,X_test,y_train,y_test):
	model.fit(X_train,y_train)
	return model.score(X_test,y_test)
kf=KFold(n_splits=32)
train_y = []
train_a = []
train_x = np.genfromtxt('train.csv',delimiter=',')
f = open("labels_0.dat","r")
for i in f:
	train_y.append(i)
train_y = np.array(train_y).astype(np.float)
train_y = train_y.astype(np.int)
train_x = np.array(train_x)
#print ("valence",train_y)
#print (train_x)
#print ("train_x",train_x)
print(train_x.shape)
print(train_y.shape)
clf = KNeighborsClassifier(n_neighbors=1)
#X_train,X_test,y_train,y_test=train_test_split(train_x,train_y,test_size=0.5)
for train_index,test_index in kf.split(train_x):
	X_train,X_test,y_train,y_test=train_x[train_index],train_x[test_index],train_y[train_index],train_y[test_index]	
predicted_val=get_score(clf,X_train,X_test,y_train,y_test)
print(predicted_val)


f = open("labels_1.dat","r")
for i in f:
	train_a.append(i)
train_a = np.array(train_a).astype(np.float)
train_a = train_a.astype(np.int)

kf1=KFold(n_splits=32)
clf1 = KNeighborsClassifier(n_neighbors=1)
#X_train1,X_test1,y_train1,y_test1=train_test_split(train_x,train_a,test_size=0.5)
for train_index,test_index in kf1.split(train_x,train_a):
	X_train1,X_test1,y_train1,y_test1=train_x[train_index],train_x[test_index],train_a[train_index],train_a[test_index]	
arousal_val=get_score(clf1,X_train1,X_test1,y_train1,y_test1)
print(arousal_val)

