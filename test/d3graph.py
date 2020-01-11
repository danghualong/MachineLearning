import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def getZ(x,y):
    return (2*x**2+3*y+3)+(y**2-9*x+6) 

xrng=np.arange(-3,3,.1)
yrng=np.arange(-4,4,.1)

# 求曲面的最小值对应的坐标
x=tf.Variable(tf.random.truncated_normal([1]))
y=tf.Variable(tf.random.truncated_normal([1]))
rate=0.1
epoches=1000
for epoch in range(epoches):
    with tf.GradientTape(persistent=True) as tape:
        loss=getZ(x,y)
    grads=tape.gradient(loss,[x,y])
    print('epoch={0},x={1},y={2},loss={3}'.format(epoch,x.numpy(),y.numpy(),loss.numpy()))
    x.assign_sub(rate*grads[0])
    y.assign_sub(rate*grads[1])



# 设置交叉点
X,Y=np.meshgrid(xrng,yrng)
Z=getZ(X,Y)

# print(X.shape,Y.shape,Z.shape)
# print(X,Y,Z)

ax=plt.gca(projection='3d')
ax.plot_surface(X,Y,Z,color='g')
# 调整透视角度，第一个是沿Z轴旋转，第二个是沿Y轴旋转
ax.view_init(3,50)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.scatter(x.numpy(),y.numpy(),loss.numpy(),color='r',marker='o')
plt.show()

