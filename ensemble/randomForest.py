import numpy as np
import utils.dataLoader as loader
from sklearn.ensemble import RandomForestClassifier

X=np.array([
    [25,179,15,0],
    [33,190,19,0],
    [28,180,18,2],
    [25,178,18,2],
    [46,100,100,2],
    [40,170,170,1],
    [34,174,20,2],
    [36,181,55,1],
    [35,170,25,2],
    [30,180,35,1],
    [28,174,30,1],
    [29,176,36,1]
])
Y=np.array([0,1,1,1,0,0,1,0,1,1,0,1])



def loadData(keepprob=0.8):
    data=loader.loadIrisData()
    m,n=data.shape
    lenTrain=int(keepprob*m)
    np.random.shuffle(data)
    x_train=data[:lenTrain,:-1]
    y_train=data[:lenTrain,-1]
    x_test=data[lenTrain:,:-1]
    y_test=data[lenTrain:,-1]
    return x_train,y_train,x_test,y_test

# x_train,y_train,x_test,y_test=loadData()
# classifier=RandomForestClassifier(n_estimators=10,max_depth=2).fit(x_train,y_train)

# test_labels=classifier.predict(x_test)
# error_rate=np.sum(y_test!=test_labels)/len(y_test)
# print("error_rate=",error_rate)

errorList=[]
MAX_DEPTH=5
for i in range(1,MAX_DEPTH):
    np.random.seed(10)
    x_train,y_train,x_test,y_test=loadData()
    classifier=RandomForestClassifier(n_estimators=5,max_depth=i)
    classifier.fit(x_train,y_train)
    test_labels=classifier.predict(x_test)
    error_rate=np.sum(y_test!=test_labels)/len(y_test)
    errorList.append(error_rate)

import matplotlib.pyplot as plt
print(errorList)
plt.plot(range(1,MAX_DEPTH),errorList)
plt.show()
   
