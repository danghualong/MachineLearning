import numpy as np
import tensorflow as tf
import mnist.mninst_util as mnistUtil
from tensorflow.keras import optimizers,layers,datasets,Sequential

LR=0.01
EPOCHES=10
BATCH_SIZE=100
CONV1_COUNT=32
CONV2_COUNT=64
CONV3_COUNT=64
DENSE1_COUNT=64
IMAGE_WIDTH=28
IMAGE_HEIGHT=28


# 预处理数据
(train_images,train_labels),(test_images,test_labels)=datasets.mnist.load_data()
testY_hot=tf.one_hot(test_labels,depth=mnistUtil.ClASS_SIZE)
testX=tf.convert_to_tensor(test_images.reshape((-1,IMAGE_WIDTH,IMAGE_HEIGHT,1)),tf.float32)
testY=tf.convert_to_tensor(testY_hot,tf.float32)
trainY_hot=tf.one_hot(train_labels,depth=mnistUtil.ClASS_SIZE)
trainX=tf.convert_to_tensor(train_images.reshape((-1,IMAGE_WIDTH,IMAGE_HEIGHT,1)),tf.float32)
trainY=tf.convert_to_tensor(trainY_hot,tf.float32)

#构建模型
model=Sequential()
model.add(layers.Conv2D(filters=CONV1_COUNT, kernel_size=(3, 3), activation='relu', input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT,1)))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=CONV2_COUNT, kernel_size=(3, 3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=CONV3_COUNT, kernel_size=(3, 3), activation='relu'))
# 展平一个张量
model.add(layers.Flatten())
model.add(layers.Dense(DENSE1_COUNT, activation='sigmoid'))
model.add(layers.Dense(mnistUtil.ClASS_SIZE, activation='softmax'))

optimizer=optimizers.SGD(lr=LR)

model.compile(optimizer=optimizer,loss='categorical_crossentropy',metrics=['accuracy'])
history=model.fit(trainX,trainY,epochs=EPOCHES,batch_size=BATCH_SIZE,verbose=1)
# plotHistory(history)
# 测试模型
(loss,accuracy)=model.evaluate(testX,testY,verbose=0)
print("测试cost={0},accuracy={1}".format(loss,accuracy))
            

