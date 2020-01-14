import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import optimizers,losses
# 在sitepackages目录中添加.pth文件，并将模块所在目录添加进去即可。
from utils.dataLoader import loadIrisData
import numpy as np

print(tf.__version__)

data=loadIrisData()
m=data.shape[0]
constantWeights=np.ones((m,1))
X=np.concatenate((data[:,:-1],constantWeights),axis=1)
# print(data)

# 使用tf构建模型
epoches=1000
rate=0.05
num_classes=3
num_attrs=X.shape[1]


Y=data[:,-1]
# print(Y)


tfX=tf.convert_to_tensor(X,dtype=tf.float32)
tfY=tf.convert_to_tensor(Y,dtype=tf.float32)



W=tf.Variable(tf.random.truncated_normal([num_attrs,num_classes]))
# optimizer=optimizers.SGD(rate)

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











