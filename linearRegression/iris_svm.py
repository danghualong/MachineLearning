import tensorflow as tf
from tensorflow.keras import optimizers,Sequential,layers
# 在sitepackages目录中添加.pth文件，并将模块所在目录添加进去即可。
from utils.dataLoader import loadIrisData
import numpy as np
import sklearn.svm as svm
import math

np.random.seed(10)
data=loadIrisData()
m=len(data)
np.random.shuffle(data)



X=data[:,:-1]
Y=data[:,-1]
train_size=90
X_train=X[:train_size]
Y_train=Y[:train_size]
X_test=X[train_size:]
Y_test=Y[train_size:]
for i in range(20):
    c=math.pow(2,i-10)
    clf=svm.SVC(C=c,kernel='linear',verbose=False,decision_function_shape='ovo')
    clf.fit(X_train,Y_train)
    ypred=clf.predict(X_test)
    accuracy=np.mean(ypred==Y_test)
    print('C={0},accuracy={1}'.format(c,accuracy))


