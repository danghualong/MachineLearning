import numpy as np
import matplotlib.pyplot as plt
import random

size=19
X=np.arange(size).astype(float)
Y=[]

for i in range(size):
    if(i%2==0):
        Y.append(3*i+1+random.random()*2)
    else:
        Y.append(3*i-1-random.random()*3)
Y=np.array(Y)

X1=[i for i in range(size) if i%2==0]
X2=[i for i in range(size) if i%2==1]
Y1=Y[X1]
Y2=Y[X2]


W=0
b=0



def getLogit(x):
    return W*x+b

def showLine():
    yhat=W*X+b
    plt.plot(X,yhat,color='r')
    plt.scatter(X1,Y1,marker='o')
    plt.scatter(X2,Y2,marker='x')
    plt.show()


times=0
while(True):
    isAllOK=True
    for i in range(size):
        logit=getLogit(X[i])
        if(i%2==1):
            while(logit<=Y[i]):
                W=W+X[i]*0.1
                b=b+0.1
                logit=getLogit(X[i])
                times+=1
                isAllOK=False
        else:
            while(logit>=Y[i]):
                W=W-X[i]*0.1
                b=b-0.1
                times+=1
                logit=getLogit(X[i])
                isAllOK=False
    print('w={0},b={1},times={2}'.format(W,b,times))
    if(isAllOK):
        showLine()
        break









