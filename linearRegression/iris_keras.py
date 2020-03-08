import tensorflow as tf
from tensorflow.keras import optimizers,Sequential,layers
# 在sitepackages目录中添加.pth文件，并将模块所在目录添加进去即可。
from utils.dataLoader import loadIrisData
import numpy as np
import math
from linearRegression.draw_util import showTrendencies


np.random.seed(10)
data=loadIrisData()
m=len(data)
np.random.shuffle(data)

X=data[:,:-1]
YLables=data[:,-1].astype(np.int16)
Y=np.eye(m,3)[YLables]

def createModel():
    model=Sequential()
    model.add(layers.Dense(3,activation='softmax',use_bias=True,kernel_initializer='ones',bias_initializer=tf.random_normal_initializer()))
    return model

accurs=[]

for i in range(8):
    model=createModel()
    index=-int(i/2)
    ratio=(2 if i%2==0 else 10)
    lr=math.pow(10,index)/ratio
    optimizer=optimizers.SGD(lr)
    model.compile(optimizer=optimizer,loss='categorical_crossentropy',metrics=['accuracy'])
    hist=model.fit(X,Y,epochs=100,verbose=2,validation_split=0.4)
    accurs.append({'lr':lr,'train_accurs':hist.history['accuracy'],'test_accurs':hist.history['val_accuracy']})

showTrendencies(accurs)
# weights=model.layers[0].get_weights()
# print(weights)


