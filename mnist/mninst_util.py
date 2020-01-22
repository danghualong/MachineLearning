import numpy as np
import tensorflow as tf
import math


PIXEL_SIZE=28*28
hiddenUnits1=16
hiddenUnits2=16
ClASS_SIZE=10

def createVars():
    W1=tf.Variable(tf.random.truncated_normal([PIXEL_SIZE,hiddenUnits1],stddev=1.0/math.sqrt(PIXEL_SIZE)))
    b1=tf.Variable(tf.random.truncated_normal([hiddenUnits1]))
    W2=tf.Variable(tf.random.truncated_normal([hiddenUnits1,hiddenUnits2],stddev=1.0/math.sqrt(hiddenUnits1)))
    b2=tf.Variable(tf.random.truncated_normal([hiddenUnits2]))
    W3=tf.Variable(tf.random.truncated_normal([hiddenUnits2,ClASS_SIZE],stddev=1.0/math.sqrt(hiddenUnits2)))
    b3=tf.Variable(tf.random.truncated_normal([ClASS_SIZE]))
    return (W1,b1,W2,b2,W3,b3)

def getLogits(X,variables):
    output1=tf.nn.relu(tf.matmul(X,variables[0])+variables[1])
    output2=tf.nn.sigmoid(tf.matmul(output1,variables[2])+variables[3])
    output3=tf.matmul(output2,variables[4])+variables[5]
    # output3=tf.matmul(x,W)+b
    return output3

def getLoss(logits,Y):
    entropy=tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=Y)
    return tf.reduce_mean(entropy)

def getAccuracy(logits,Y):
    sm_logits=tf.nn.softmax(logits)
    predictMaxList=tf.argmax(sm_logits,1)
    actualMaxList=tf.argmax(Y,1)
    pred=tf.cast(tf.equal(predictMaxList,actualMaxList),tf.float32)
    accur=tf.reduce_mean(pred)
    return accur