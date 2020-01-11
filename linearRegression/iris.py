import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import optimizers,losses
import pandas as pd
import numpy as np
import os
dirName=dirName=os.path.dirname(__file__)


# print(pd.__version__)
# print(keras.__version__)

data=pd.read_csv(dirName+'/iris.data',header=None,names=['x1','x2','x3','x4','y'])


# data=np.load('./data/iris.npy',allow_pickle=True)

class_mapping={'Iris-virginica':2,'Iris-versicolor':1,'Iris-setosa':0}
data.iloc[:,4]=data.iloc[:,4].map(class_mapping)
data.insert(4,'c',1)

# print(data)
epoches=1000
rate=0.05
num_classes=3
num_attrs=5


X=np.array(data.iloc[:,0:num_attrs])
singleY=np.array(data.iloc[:,-1])
Y=np.eye(num_classes)[singleY]


tfX=tf.convert_to_tensor(X,dtype=tf.float32)
tfY=tf.convert_to_tensor(Y,dtype=tf.float32)



W=tf.Variable(tf.random.truncated_normal([num_attrs,num_classes]))
optimizer=optimizers.SGD(rate)

for epoch in range(epoches):
    with tf.GradientTape() as tape:
        logits=tf.matmul(tfX,W)
        cross_entropy=tf.nn.softmax_cross_entropy_with_logits(labels=tfY,logits=logits)
        loss=tf.reduce_mean(cross_entropy)
    grads=tape.gradient(loss,W)
    W.assign_sub(rate*grads.numpy())
    # optimizer.apply_gradients(zip(grads,W))
    # if((epoch+1)%10==0):
    #     print('epoch={0},w={1},loss={2}'.format(epoch+1,W.numpy(),loss.numpy()))

pred=tf.nn.softmax(tf.matmul(tfX,W))
print(tf.argmax(pred,axis=1).numpy())









