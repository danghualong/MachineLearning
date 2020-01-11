import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras import optimizers,layers
import random


epoches=200
batchSize=10

X=np.arange(0,10,0.1)
Y=2*X+3

tfX=tf.convert_to_tensor(X,dtype=tf.float32)
tfY=tf.convert_to_tensor(Y,dtype=tf.float32)

w=tf.Variable(np.random.randn(),dtype=tf.float32)
b=tf.Variable(np.random.randn(),dtype=tf.float32)

traindb=tf.data.Dataset.from_tensor_slices((tfX,tfY)).batch(10).repeat(80)

optimizer=optimizers.SGD(lr=0.01)


for epoch in range(epoches):
    indices=np.arange(len(X))
    random.shuffle(indices)
    startIndex=0
    while(startIndex+batchSize<len(X)):
        x=X[indices[startIndex:startIndex+batchSize]]
        y=Y[indices[startIndex:startIndex+batchSize]]
        with tf.GradientTape() as tape:
            predict=w*x+b
            loss=tf.reduce_mean(tf.square(predict-y))
        grads=tape.gradient(loss,[w,b])
        optimizer.apply_gradients(zip(grads,[w,b]))
        startIndex+=batchSize
    if((epoch+1)%10==0):
        print('epoch:{0},w:{1:.3f},b:{2:.3f},loss:{3:.3f}'.format((epoch+1),w.numpy(),b.numpy(),loss.numpy()))
    





