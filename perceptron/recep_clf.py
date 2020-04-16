import numpy as np
import matplotlib.pyplot as plt
import random

class Perceptron(object):
    def __init__(self):
        self.w=None
        self.b=0
        self.lr=1

    def fit(self,X,Y):
        size=len(Y)
        self.w=np.zeros(X.shape[1])
        self.b=0
        times=0
        while(True):
            isAllOK=True
            for i in range(size):
                logit=Y[i]*(np.dot(self.w,X[i])+self.b)
                if(logit<=0):
                    self.w=self.w+self.lr*Y[i]*X[i]
                    self.b=self.b+self.lr*Y[i]
                    isAllOK=False
            times+=1
            if(isAllOK):
                print("times:",times)
                self._showLine(X,Y)
                break

    def predict(self,testX):
        return np.dot(self.w,testX)+self.b

    def _showLine(self,X,Y):
        yhat=-(self.w[0]*X[:,0]+self.b)/self.w[-1]
        plt.plot(X[:,0],yhat,color='r')
        classes=Y[:,0]
        plt.scatter(X[classes>0,0],X[classes>0,-1],marker='o')
        plt.scatter(X[classes<0,0],X[classes<0,-1],marker='x')
        plt.show()


if __name__=='__main__':
    np.random.seed(100)
    size=19
    wt=(3,-1)
    bt=2
    rands=np.random.random(size)
    X1=np.random.random([size,1])*5
    X2=wt[0]*X1+bt-random.random()*2
    X2[rands>0.5]=wt[0]*X1[rands>0.5]+bt+random.random()*2
    X=np.hstack((X1,X2))

    Y=np.ones([size,1])
    Y[rands<=0.5]=-1
    
    clf=Perceptron()
    clf.fit(X,Y)
    print(clf.predict((3,-12)))

    








