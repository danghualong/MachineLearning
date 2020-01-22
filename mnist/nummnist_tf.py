import numpy as np
import tensorflow as tf
import math
import mnist.mninst_util as mnistUtil

tf.compat.v1.disable_eager_execution()

lr=0.01
validation_size=10000
BATCH_SIZE=100
EPOCHES=10

data=np.load(r'C:\Users\Administrator\.keras\datasets\mnist.npz')
print(data.files)
xtrain=data['x_train'].reshape(-1,mnistUtil.PIXEL_SIZE)
ytrain=np.eye(mnistUtil.ClASS_SIZE)[data['y_train']]
xtest=data['x_test'].reshape(-1,mnistUtil.PIXEL_SIZE)
ytest=np.eye(mnistUtil.ClASS_SIZE)[data['y_test']]

x=tf.compat.v1.placeholder(tf.float32,(None,mnistUtil.PIXEL_SIZE))
y=tf.compat.v1.placeholder(tf.float32,(None,mnistUtil.ClASS_SIZE))


def shuffleData(x,y):
    m=len(x)
    indices=np.arange(m)
    np.random.shuffle(indices)
    return x[indices],y[indices]

def getBatchData(x,y,batchNum,batchSize):
    start=batchNum*batchSize
    end=start+batchSize
    return x[start:end],y[start:end]
# Variables在global_variables_initializer 会被初始化
variables=mnistUtil.createVars()
logits=mnistUtil.getLogits(x,variables)
cost=mnistUtil.getLoss(logits,y)
accur=mnistUtil.getAccuracy(logits,y)
target=tf.compat.v1.train.GradientDescentOptimizer(lr).minimize(cost)
init=tf.compat.v1.global_variables_initializer()
accurList=[]

with tf.compat.v1.Session() as sess:
    sess.run(init)
    for i in range(EPOCHES):
        shuffleX,shuffleY=shuffleData(xtrain,ytrain)
        batchNum=int(len(xtrain)/BATCH_SIZE)
        for j in range(batchNum):
            xbatch,ybatch=getBatchData(shuffleX,shuffleY,j,BATCH_SIZE)
            _,loss=sess.run((target,cost),feed_dict={x:xbatch,y:ybatch})
            if((j+1)%50==0):
                print("epoch={0},batchNum={1},loss={2}".format(i+1,j+1,loss))
        test_accuracy=sess.run((accur),feed_dict={x:xtest,y:ytest})
        accurList.append(test_accuracy)
        print("epoch={0},test_accuracy={1}".format(i+1,test_accuracy))
        if((i+1)%5==0):
            train_accuracy=sess.run(accur,feed_dict={x:xtrain,y:ytrain})
            print("epoch={0},train_accuracy={1}".format(i+1,train_accuracy))
                    
import matplotlib.pyplot as plt
epoches=np.arange(EPOCHES)
plt.plot(epoches,accurList)
plt.show()    

