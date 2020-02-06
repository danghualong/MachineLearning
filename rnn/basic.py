import numpy as np
import tensorflow as tf
import tensorflow.compat.v1.nn as nn
import rnn.rnn_util as rnnUtil


tf.compat.v1.disable_eager_execution()

TIME_STEPS=28   #时序长度(即28个时刻)
NUM_INPUT=28    #每个时刻输入的一个向量(即28个像素)
NUM_HIDDEN=64   #每个隐藏层的节点数
LAYERS_NUM=2    #隐藏层数
CLASSES=10      #输出向量长度
LEARNING_RATE=0.1
EPOCHES=20
BATCH_SIZE=128


xtrain,ytrain,xtest,ytest=rnnUtil.loadData(TIME_STEPS,NUM_INPUT,CLASSES)

X=tf.compat.v1.placeholder(tf.float32,[None,TIME_STEPS,NUM_INPUT])
Y=tf.compat.v1.placeholder(tf.float32,[None,CLASSES])

weights={
    'out':tf.Variable(tf.random.normal([NUM_HIDDEN,CLASSES]))
}

bias={
    'out':tf.Variable(tf.random.normal([CLASSES]))
}

def inference(X,weights,bias):
    # TimeSteps个向量(X1,X2...X28)
    x_seqs=tf.unstack(X,TIME_STEPS,1)
    # 创建每个时序的Cell
    cell=nn.rnn_cell.LSTMCell(NUM_HIDDEN)
    outputs,states=tf.compat.v1.nn.static_rnn(cell,x_seqs,dtype=tf.float32)
    # outputs,states=tf.compat.v1.nn.dynamic_rnn(cell,X,dtype=tf.float32)
    # 在输出层计算预测值yhat
    return tf.matmul(outputs[-1],weights)+bias



logits=inference(X,weights['out'],bias['out'])
loss=tf.reduce_mean(tf.compat.v1.nn.softmax_cross_entropy_with_logits_v2(Y,logits))
optimizer=tf.compat.v1.train.GradientDescentOptimizer(LEARNING_RATE)
target=optimizer.minimize(loss)
init=tf.compat.v1.global_variables_initializer()
accuracy=rnnUtil.getAccuracy(logits,Y)

with tf.compat.v1.Session() as sess:
    sess.run(init)
    for i in range(EPOCHES):
        iterNum=len(xtrain)//BATCH_SIZE
        for j in range(iterNum):
            xbatch=xtrain[j*BATCH_SIZE:(j+1)*BATCH_SIZE,:].reshape([-1,TIME_STEPS,NUM_INPUT])
            ybatch=ytrain[j*BATCH_SIZE:(j+1)*BATCH_SIZE,:]
            sess.run(target,feed_dict={X:xbatch,Y:ybatch})
        loss_val,accuracy_val=sess.run((loss,accuracy),feed_dict={X:xbatch,Y:ybatch})
        print("\nEPOCH={0},loss={1},accuracy={2}".format((i+1),loss_val,accuracy_val))
    accuracy_test=sess.run(accuracy,feed_dict={X:xtest,Y:ytest})
    print("\ntest accuracy={0}".format(accuracy_test))

def training():
    pass
