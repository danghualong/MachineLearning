import numpy as np
import tensorflow as tf

def loadData(timesteps,inputSize,classes):
    data=np.load(r'C:\Users\Administrator\.keras\datasets\mnist.npz')
    xtrain=data['x_train'].reshape(-1,timesteps,inputSize)
    ytrain=np.eye(classes)[data['y_train']]
    xtest=data['x_test'].reshape(-1,timesteps,inputSize)
    ytest=np.eye(classes)[data['y_test']]
    return xtrain,ytrain,xtest,ytest

def getAccuracy(logits,Y):
    sm_logits=tf.nn.softmax(logits)
    predictMaxList=tf.argmax(sm_logits,1)
    actualMaxList=tf.argmax(Y,1)
    pred=tf.cast(tf.equal(predictMaxList,actualMaxList),tf.float32)
    accur=tf.reduce_mean(pred)
    return accur