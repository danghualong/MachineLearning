import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


X=np.arange(-3,3,0.1)
Y=2*X+3

tfX=tf.convert_to_tensor(X,tf.float32)
tfY=tf.convert_to_tensor(Y,tf.float32)

w=tf.constant(tf.random.truncated_normal([1]))
b=tf.constant(tf.random.truncated_normal([1]))
rate=0.01
epoches=2000

for epoch in range(epoches):
    # 设置跟踪器
    with tf.GradientTape() as tape:
        # 对于constant参数，需要进行watch操作；如果是variable，则不需要此句
        tape.watch([w,b]) 
        # 计算损失函数
        pred=tf.add(tf.multiply(w,tfX),b)
        loss=tf.reduce_mean(tf.square(pred-tfY))
    # 求解梯度向量
    grads=tape.gradient(loss,[w,b])
    s_loss=loss.numpy()
    print('epoch={3},w={0},b={1},loss={2}'.format(w.numpy(),b.numpy(),s_loss,epoch))
    # 利用梯度向量进行BP操作
    w-=rate*grads[0]
    b-=rate*grads[1]
    # 如果w,b是variable,则只能用如下方法进行BP操作
    # w.assign_sub(rate*grads[0])
    # b.assign_sub(rate*grads[1])
    if(s_loss<1e-5):
        break








    