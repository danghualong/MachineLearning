import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import optimizers,layers

import matplotlib.pyplot as plt

fmnist=keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels)=fmnist.load_data()


for i in range(12):
    plt.subplot(3,4,(i+1))
    plt.xticks([])
    plt.yticks([])
    plt.imshow(train_images[i])
    plt.grid(False)
plt.show()