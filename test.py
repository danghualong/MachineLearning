import numpy as np
import matplotlib.pyplot as plt
from abc import ABCMeta,abstractmethod
import tensorflow as tf
from scipy.stats import norm


class Context(metaclass=ABCMeta):
    def __init__(self):
        self._state=CloseState(self)

    def setState(self,state):
        self._state=state
    
    def getState(self):
        return self._state
    
    def open(self):
        self._state.open()

    def close(self):
        self._state.close()

class State(metaclass=ABCMeta):
    def __init__(self,context):
        self._context=context
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def close(self):
        pass

def singleton(cls):
    def _singleton(cls,*args,**kwargs):
        if not hasattr(cls, "_instance"):
            print("hhe")
            cls._instance = cls(*args, **kwargs)
        return cls._instance
    return _singleton

class OpenState(State):
    def open(self):
        print("have already open")
    def close(self):
        self._context.setState(CloseState(self._context))
        print('changed State')

class CloseState(State):
    def open(self):
        self._context.setState(OpenState(self._context))
        print('changed State')
    def close(self):
        print("have already closed")

def showMultiEigenLines():
    xs=np.array([[2.4,4,5,7],[2.6,5.5,6,8],[3.9,5,4.7,9],[4.1,5.7,4.7,10],[3.8,5,4.7,9]])
    m,n=xs.shape
    for i in range(n):
        plt.plot(xs[:,i],c=plt.cm.RdYlBu(i/n+0.4),label='attr{0}'.format((i+1)))
    plt.legend(loc='lower right')
    plt.show()

def showRandomImages():
    from matplotlib.image import imread

    from scipy import ndimage

    
    data=imread('./dr/data/niu.jpg')
    # data=np.array(np.random.randint(0,256,(400,500,3),dtype=np.uint8))
    fig=plt.figure()
    fig.add_subplot(321)
    plt.axis('off')
    plt.imshow(data[:,:,0],cmap=plt.cm.gray)
    plt.title('R channel')
    fig.add_subplot(322)
    plt.axis('off')
    plt.imshow(data[:,:,1],cmap=plt.cm.gray)
    plt.title('G channel')
    fig.add_subplot(323)
    plt.axis('off')
    plt.imshow(data[:,:,2],cmap=plt.cm.gray)
    plt.title('B channel')
    fig.add_subplot(324)
    plt.axis('off')
    plt.imshow(data)
    plt.title('origin')
    
    fig.add_subplot(325)
    plt.axis('off')
    kernel=np.ones((3,3))*-1
    kernel[1,1]=8
    m,n,c=data.shape
    flatImage=data.reshape(m,n*c)
    covImage=ndimage.convolve(flatImage,kernel)
    plt.imshow(covImage.reshape(m,n,c))
    plt.title('convolved')

    plt.show()

def setLabel(x):
    result=np.zeros((len(x)))
    result[x[:,0]<5]=1
    result[np.all((x[:,0]>=5,x[:,1]<5),axis=0)]=2
    return result

def drawRegions(x1,x2,func,cmap):
    t1,t2=np.meshgrid(x1,x2)
    t=np.stack((t1.flat,t2.flat),axis=1)
    # print(t)
    labels=setLabel(t)
    plt.pcolormesh(t1,t2,labels.reshape(t1.shape),cmap=cmap)
    plt.show()

def drawHist():
    u=np.random.uniform(0,1,10000)
    # plt.hist(u,80,facecolor='g',alpha=0.7)
    # plt.show()
    times=10000
    for i in range(times):
        u+=np.random.uniform(0,1,10000)
    u/=times
    plt.figure(facecolor='c')
    plt.hist(u,50,color='g',edgecolor='k',alpha=0.7)
    plt.grid(True)
    plt.show()
 

if __name__=='__main__':
    arr=np.arange(20).reshape(2,10)
    print(arr)
    sums=np.sum(arr,axis=1)
    print(sums)
    



                
            