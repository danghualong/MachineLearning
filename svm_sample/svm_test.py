import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from Classifier.Classifier.dataLoader import loadData

mat,labels=loadData("./Classifier/Classifier/samples/data1.txt")
X=np.array(mat)
Y=np.array(labels)

def showPoints(X,Y):
    X_class1=X[np.argwhere(Y==1).reshape(-1)]
    X_class2=X[np.argwhere(Y==-1).reshape(-1)]

    plt.scatter(X_class1[:,0],X_class1[:,1],marker='^',c='r')
    plt.scatter(X_class2[:,0],X_class2[:,1],marker='o',c='g')
    plt.show()
trainSize=int(0.8*len(X))
Xtrain=X[:trainSize]
Ytrain=Y[:trainSize]
Xtest=X[trainSize:]
Ytest=Y[trainSize:]
clf=SVC(kernel='linear',verbose=True)
clf.fit(Xtrain,Ytrain)
Ypred=clf.predict(Xtest)
ratio=np.mean(Ypred==Ytest)
print("ratio:",ratio)