from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import KFold,train_test_split
def get_score(model,X_train,X_test,y_train,y_test): #this function is used to check the accuracy score for a given model, training and testing data
	model.fit(X_train,y_train)
	return model.score(X_test,y_test)
kf=KFold(n_splits=10)
train_y = [] #Actual result of the data used in testing of the valence 
train_a = [] #Actual result of the data used in testing of the arousal
train_x = np.genfromtxt('traina.csv',delimiter=',',skip_header=0)
train_x = np.array(train_x)
train_x=train_x.astype(np.long)
f = open("labels_0.dat","r")
for i in f:
	train_y.append(i) #copying data from the file to the list
train_y = np.array(train_y).astype(np.float)
train_y = train_y.astype(np.int)#changing the list to numpy array and its value type from float to int


clf = KNeighborsClassifier(n_neighbors=3) #knn model for classifying the valence

for train_index,test_index in kf.split(train_x):
	X_train,X_test,y_train,y_test=train_x[train_index],train_x[test_index],train_y[train_index],train_y[test_index]	

predicted_val=get_score(clf,X_train,X_test,y_train,y_test)
print( predicted_val)


f = open("labels_1.dat","r")
for i in f:
	train_a.append(i) #copying data from the file to the list
train_a = np.array(train_a).astype(np.float)
train_a = train_a.astype(np.int) #changing the list to numpy array and its value type from float to int


kf1=KFold(n_splits=10)
clf1 = KNeighborsClassifier(n_neighbors=3) #knn model for classifying the valence

for train_index,test_index in kf1.split(train_x):
	X_train1,X_test1,y_train1,y_test1=train_x[train_index],train_x[test_index],train_a[train_index],train_a[test_index]
arousal_val=get_score(clf1,X_train1,X_test1,y_train1,y_test1)
print(arousal_val)
