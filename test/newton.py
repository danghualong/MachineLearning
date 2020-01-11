import math
import numpy as  np
import matplotlib.pyplot as plt
#牛顿法求解方程的解

def getMinValue(a,b,c):
    x0=0
    y=a*math.pow(x0,2)+b*x0+c
    x1=x0-y/(2*a*x0+b)
    # print(x0,x1,math.fabs(x0-x1))
    while(math.fabs(x0-x1)>0.00000001):
        x0=x1
        y=a*math.pow(x0,2)+b*x0+c
        x1=x0-y/(2*a*x0+b)
    return x0

a=-1
b=2
c=1


xMin=getMinValue(a,b,c)

X=np.arange(-5,5,0.1)
Y=a*X**2+b*X+c
plt.plot(X,Y,'k-')
plt.plot(X,np.zeros((len(X))),'k-')

yMin=a*xMin**2+b*xMin+c
plt.annotate('({0:.2f},{1:.2f})'.format(xMin,yMin),(xMin,yMin),xytext=(xMin+0.2,yMin+0.1))
plt.scatter(xMin,yMin,c='r',marker='o')


plt.show()


