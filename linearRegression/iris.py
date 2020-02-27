import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import optimizers,losses
# 在sitepackages目录中添加.pth文件，并将模块所在目录添加进去即可。
from utils.dataLoader import loadIrisData
import numpy as np
from linearRegression.draw_util import showOneTrendency

# print(tf.__version__)
# print(tf.__path__)

data=loadIrisData()
m=data.shape[0]
X=data[:,:-1]
mean=np.mean(X,axis=0)
std=np.std(X,axis=0)
X=(X-mean)/std

constantWeights=np.ones((m,1))
X=np.concatenate((data[:,:-1],constantWeights),axis=1)

# X=data[:,:-1]

# print(data)

# 使用tf构建模型
epoches=1000
rate=0.01
num_classes=3
num_attrs=X.shape[1]


Y=data[:,-1:]
# print(Y)






train_size=90
accurs=[]

for epoch in range(epoches):
    print('epoch=',(epoch+1))
    indices=np.random.shuffle(np.arange(len(X)))
    X_train=X[:train_size]
    Y_train=Y[:train_size]
    X_test=X[train_size:]
    Y_test=Y[train_size:]
    tfX=tf.convert_to_tensor(X_train,dtype=tf.float32)
    tfY=tf.convert_to_tensor(Y_train,dtype=tf.float32)
    W=tf.Variable(tf.random.truncated_normal([num_attrs,num_classes]))
    with tf.GradientTape() as tape:
        logits=tf.matmul(tfX,W)
        cross_entropy=tf.nn.softmax_cross_entropy_with_logits(labels=tfY,logits=logits)
        loss=tf.reduce_mean(cross_entropy)
    grads=tape.gradient(loss,W)
    W.assign_sub(rate*grads.numpy())
    # optimizer.apply_gradients(zip(grads,W))
    if((epoch+1)%100==0):
        print('epoch={0},w={1},loss={2}'.format(epoch+1,W.numpy(),loss.numpy()))
    tf_testX=tf.convert_to_tensor(X_test,dtype=tf.float32)
    pred=tf.nn.softmax(tf.matmul(tf_testX,W))
    pred=tf.argmax(pred,axis=1)
    accuracy=np.mean(pred==Y_test)
    accurs.append(accuracy)
showOneTrendency(accurs)











