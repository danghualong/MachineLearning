import numpy as np
import tensorflow as tf
from tensorflow.keras import optimizers
import mnist.mninst_util as mnistUtil

# 超参数设置
LR=0.01
EPOCHES=10
BATCH_SIZE=100

# 预处理数据
(train_images,train_labels),(test_images,test_labels)=tf.keras.datasets.mnist.load_data()
testY_hot=tf.one_hot(test_labels,depth=mnistUtil.ClASS_SIZE)
testX=tf.convert_to_tensor(test_images.reshape((-1,mnistUtil.PIXEL_SIZE)),tf.float32)
testY=tf.convert_to_tensor(testY_hot,tf.float32)
trainY_hot=tf.one_hot(train_labels,depth=mnistUtil.ClASS_SIZE)
trainX=tf.convert_to_tensor(train_images.reshape((-1,mnistUtil.PIXEL_SIZE)),tf.float32)
trainY=tf.convert_to_tensor(trainY_hot,tf.float32)

# 训练模型
accurList=[]
# 初始化变量
variables=mnistUtil.createVars()
optimizer=optimizers.SGD(LR)
for i in range(EPOCHES):
    batchNum=int(trainX.shape[0]/BATCH_SIZE)
    for j in range(batchNum):
        X=trainX[j*BATCH_SIZE:(j+1)*BATCH_SIZE]
        Y=trainY[j*BATCH_SIZE:(j+1)*BATCH_SIZE]
        with tf.GradientTape() as tape:
            logits=mnistUtil.getLogits(X,variables)
            loss=mnistUtil.getLoss(logits,Y)
        grads=tape.gradient(loss,variables)
        optimizer.apply_gradients(zip(grads,variables))
        if((j+1)%100==0):
            print("epoch={0},batchNum={1},loss={2}".format(i+1,j+1,loss))
    logits=mnistUtil.getLogits(testX,variables)
    accuracy=mnistUtil.getAccuracy(logits,testY)
    accurList.append(accuracy)
    print("epoch={0},accuracy={1}".format(i+1,accuracy))

import matplotlib.pyplot as plt
epoches=np.arange(EPOCHES)
plt.plot(epoches,accurList)
plt.show()    
