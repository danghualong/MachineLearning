import tensorflow as tf
from tensorflow.keras import optimizers,Sequential,layers
# 在sitepackages目录中添加.pth文件，并将模块所在目录添加进去即可。
from utils.dataLoader import loadIrisData
import numpy as np
import matplotlib.pyplot as plt
import math

data=loadIrisData()
X=data[:,:-1]
YLables=data[:,-1].astype(np.int16)
m=len(YLables)
Y=np.eye(m,3)[YLables]

def showTrendency(train_accurs,valid_accurs):
    plt.plot(np.arange(len(train_accurs)),train_accurs,color='r',label='train')
    plt.plot(np.arange(len(valid_accurs)),valid_accurs,color='g',label='valid')
    plt.legend()
    plt.show()

for i in range(8):
    model=Sequential()
    model.add(layers.Dense(3,activation='softmax',use_bias=True,kernel_initializer='ones',bias_initializer=tf.random_normal_initializer()))
    index=-int(i/2)
    ratio=(2 if i%2==0 else 10)
    lr=math.pow(10,index)/ratio
    optimizer=optimizers.SGD(lr)
    model.compile(optimizer=optimizer,loss='categorical_crossentropy',metrics=['accuracy'])
    hist=model.fit(X,Y,epochs=100,verbose=2,validation_split=0.4)
    showTrendency(hist.history['accuracy'],hist.history['val_accuracy'])
weights=model.layers[0].get_weights()
print(weights)


