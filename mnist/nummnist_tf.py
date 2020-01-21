import numpy as np
import tensorflow as tf
import math

tf.compat.v1.disable_eager_execution()

lr=0.01
validation_size=10000
hiddenUnits1=16
hiddenUnits2=16
ClASS_SIZE=10
PIXEL_SIZE=28*28
BATCH_SIZE=100
EPOCHES=10

data=np.load(r'C:\Users\danghualong\.keras\datasets\mnist.npz')
print(data.files)
xtrain=data['x_train'].reshape(-1,PIXEL_SIZE)
ytrain=np.eye(ClASS_SIZE)[data['y_train']]
xtest=data['x_test'].reshape(-1,PIXEL_SIZE)
ytest=np.eye(ClASS_SIZE)[data['y_test']]



W1=tf.Variable(tf.random.truncated_normal([PIXEL_SIZE,hiddenUnits1],stddev=1.0/math.sqrt(PIXEL_SIZE)))
b1=tf.Variable(tf.random.truncated_normal([hiddenUnits1]))
W2=tf.Variable(tf.random.truncated_normal([hiddenUnits1,hiddenUnits2],stddev=1.0/math.sqrt(hiddenUnits1)))
b2=tf.Variable(tf.random.truncated_normal([hiddenUnits2]))
W3=tf.Variable(tf.random.truncated_normal([hiddenUnits2,ClASS_SIZE],stddev=1.0/math.sqrt(hiddenUnits2)))
b3=tf.Variable(tf.random.truncated_normal([ClASS_SIZE]))

# W=tf.Variable(tf.zeros([PIXEL_SIZE,ClASS_SIZE]))
# b=tf.Variable(tf.zeros([ClASS_SIZE]))

x=tf.compat.v1.placeholder(tf.float32,(None,PIXEL_SIZE))
y=tf.compat.v1.placeholder(tf.float32,(None,ClASS_SIZE))

def getLogits():
    output1=tf.nn.sigmoid(tf.matmul(x,W1)+b1)
    output2=tf.nn.sigmoid(tf.matmul(output1,W2)+b2)
    output3=tf.matmul(output2,W3)+b3
    # output3=tf.matmul(x,W)+b
    return output3

def getLoss(logits):
    entropy=tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=y)
    return tf.reduce_mean(entropy)

def shuffleData(x,y):
    m=len(x)
    indices=np.arange(m)
    np.random.shuffle(indices)
    return x[indices],y[indices]

def getBatchData(x,y,batchNum,batchSize):
    start=batchNum*batchSize
    end=start+batchSize
    return x[start:end],y[start:end]

def getAccuracy(logits):
    sm_logits=tf.nn.softmax(logits)
    predictMaxList=tf.argmax(sm_logits,1)
    actualMaxList=tf.argmax(y,1)
    pred=tf.cast(tf.equal(predictMaxList,actualMaxList),tf.float32)
    accur=tf.reduce_mean(pred)
    return accur

logits=getLogits()
cost=getLoss(logits)
accur=getAccuracy(logits)
target=tf.compat.v1.train.GradientDescentOptimizer(lr).minimize(cost)
init=tf.compat.v1.global_variables_initializer()
accurList=[]

with tf.compat.v1.Session() as sess:
    sess.run(init)
    for i in range(EPOCHES):
        # shuffleX,shuffleY=shuffleData(xtrain,ytrain)
        batchNum=int(len(xtrain)/BATCH_SIZE)
        for j in range(batchNum):
            xbatch,ybatch=getBatchData(xtrain,ytrain,j,BATCH_SIZE)
            _,loss=sess.run((target,cost),feed_dict={x:xbatch,y:ybatch})
            if((j+1)%50==0):
                print("epoch={0},batchNum={1},loss={2}".format(i+1,j,loss))
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

