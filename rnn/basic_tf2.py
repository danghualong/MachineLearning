import numpy as np
import tensorflow as tf
from tensorflow.keras import layers,optimizers,Sequential
import rnn.rnn_util as rnnUtil

TIME_STEPS=28   #时序长度(即28个时刻)
NUM_INPUT=28    #每个时刻输入的一个向量(即28个像素)
NUM_HIDDEN=64   #每个隐藏层的节点数
LAYERS_NUM=2    #隐藏层数
CLASSES=10      #输出向量长度
LEARNING_RATE=0.1
EPOCHES=20
BATCH_SIZE=128

xtrain,ytrain,xtest,ytest=rnnUtil.loadData(TIME_STEPS,NUM_INPUT,CLASSES)

def crateModel():
    model=Sequential()
    model.add(layers.LSTM(NUM_HIDDEN,input_shape=(TIME_STEPS,NUM_INPUT),return_sequences=True))
    model.add(layers.LSTM(NUM_HIDDEN//2))
    model.add(layers.Dense(CLASSES, activation='softmax'))
    return model
model=crateModel()
model.summary()
model.compile(loss='categorical_crossentropy',optimizer=optimizers.SGD(LEARNING_RATE),metrics=['accuracy'])
model.fit(xtrain,ytrain,batch_size=BATCH_SIZE,epochs=EPOCHES,verbose=2,shuffle=True,validation_split=0.2)
loss,accuracy=model.evaluate(xtest,ytest,verbose=0)
print("loss={0},accuracy={1}".format(loss,accuracy))