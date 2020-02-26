import numpy as np
import random
import tensorflow as tf
from tensorflow.keras import optimizers,layers,Sequential,regularizers,constraints,losses
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def getY(x1,x2):
    y=x1**2+3*x2**2-7*x1*x2+6*x1+4*x2+2+random.random()
    return y

def normalize(x):
    return ((x-np.min(x))/(np.max(x)-np.min(x))).reshape(-1,1)


np.random.seed(10)
lr=0.05
size=100

x1=np.linspace(-5,10,size)
x2=np.linspace(1,4,size)
x1square=x1**2
x2square=x2**2
x1x2=x1*x2

x1square_norm=normalize(x1square)
x2square_norm=normalize(x2square)
x1x2_norm=normalize(x1x2)
x1_norm=normalize(x1)
x2_norm=normalize(x2)

x=np.hstack((x1square_norm,x2square_norm,x1x2_norm,x1_norm,x2_norm))
y=getY(x1_norm,x2_norm)


optimizer=tf.keras.optimizers.SGD(lr)


model=Sequential()
model.add(layers.Dense(units=1,kernel_initializer=tf.random_normal_initializer()
,bias_initializer=tf.random_normal_initializer()))

model.compile(optimizer=optimizer,loss='mse')
model.fit(x,y,validation_split=0.2,epochs=100,verbose=2)
weights=model.layers[0].get_weights()
print(weights)




def getLoss(x,w,y):
    yhat=x@w
    loss=tf.reduce_mean((yhat-y)**2)
    return loss


def plotLosses(*args):
    count=len(args)
    fig=plt.figure()
    for i in range(1,count+1):
        ax=fig.add_subplot(1,1,1)
        losses=args[i-1]    
        m=len(losses)
        ax.plot(np.arange(1,(m+1)),losses)
    plt.show()    


def plot(x1,x2):
    ds1,ds2=np.meshgrid(x1,x2)
    Y=getY(ds1,ds2)
    ax=plt.gca(projection='3d')
    ax.plot_surface(ds1,ds2,Y)
    plt.show()




