import numpy as np
import tensorflow.keras as keras
import matplotlib.pyplot as plt


(trainX,trainY),(testX,testY)=keras.datasets.mnist.load_data()

weights=tf.Variable()


for i in range(12):
    plt.subplot(3,4,(i+1))
    plt.xticks([])
    plt.yticks([])
    plt.imshow(trainX[i])
    plt.grid(False)
plt.show()



