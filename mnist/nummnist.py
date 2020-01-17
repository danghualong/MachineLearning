import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential,optimizers
from tensorflow.keras.layers import Flatten,Dense
from tensorflow.keras.models import load_model,save_model
import matplotlib.pyplot as plt


def plotHistory(history):
    if(history==None):
        return
    plt.plot(history.epoch,history.history.get('accuracy'),label='accuracy')
    plt.show()

def drawSamples():
    for i in range(12):
        plt.subplot(3,4,(i+1))
        plt.xticks([])
        plt.yticks([])
        plt.imshow(testX[i])
        plt.grid(False)
    plt.show()

# 超参数设置
LR=0.01
IMAGE_SIZE=(28,28)
HIDDEN_UNITS_1=32
CLASSES=10
EPOCHES=1
BATCH_SIZE=100

# 预处理数据
(train_images,train_labels),(test_images,test_labels)=tf.keras.datasets.mnist.load_data()
testY_hot=tf.one_hot(test_labels,depth=10)
testX=tf.convert_to_tensor(test_images,tf.float32)
testY=tf.convert_to_tensor(testY_hot,tf.float32)
trainY_hot=tf.one_hot(train_labels,depth=10)
trainX=tf.convert_to_tensor(train_images,tf.float32)
trainY=tf.convert_to_tensor(trainY_hot,tf.float32)

# 创建模型
model=Sequential()
model.add(Flatten(input_shape=IMAGE_SIZE))
model.add(Dense(HIDDEN_UNITS_1,activation='sigmoid'))
# model.add(Dense(16,activation='sigmoid'))
model.add(Dense(CLASSES,activation='softmax'))

# 训练模型
optimizer=optimizers.SGD(LR)
model.compile(optimizer=optimizer,loss='categorical_crossentropy',metrics=['accuracy'])
history=model.fit(trainX,trainY,epochs=EPOCHES,batch_size=BATCH_SIZE,verbose=0)
plotHistory(history)
# 测试模型
(loss,accuracy)=model.evaluate(testX,testY,verbose=0)
print("测试cost={0},accuracy={1}".format(loss,accuracy))
# 保存模型
save_model(model,'./mnist/models/mymnist.h5')
del model

#加载模型，并应用模型
# model=load_model('./mnist/models/mymnist.h5')
# result=model.predict_classes(testX[:10,:,:],verbose=0)
# print(result)
# print(tf.argmax(testY[0:10,:],axis=1).numpy())
# drawSamples()






