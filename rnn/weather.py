import numpy as np
import tensorflow as tf
import pandas as pd
from tensorflow.keras import layers,Sequential,optimizers
from datetime import datetime as dt
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder


def parsedate(x):
    return dt.strptime(x, '%Y %m %d %H')
def process_raw_data():
    df=pd.read_csv('./rnn/data/prsa.csv',parse_dates=[['year','month','day','hour']],date_parser=parsedate,index_col=0)
    df.drop('No',inplace=True,axis=1)
    df.columns=['pollution','dewp','temp','press','wnd_dir','wnd_speed','snow','rain']
    df.index.name='date'
    df['pollution'].fillna(0,inplace=True)
    df=df[24:]
    df.to_csv('./rnn/data/pollution.csv')

def getPredictColumn(data,offset,col_index):
    pred_col=data[offset:,col_index]
    data=np.hstack((data[:-offset],pred_col.reshape(-1,1)))
    return data

def preprocess():
    df=pd.read_csv('./rnn/data/pollution.csv',header=0,index_col=0)
    data=df.values
    encoder=LabelEncoder()
    data[:,4]=encoder.fit_transform(data[:,4])
    data=data.astype('float')
    scaler=MinMaxScaler(feature_range=(0,1))
    data=scaler.fit_transform(data)
    data=getPredictColumn(data,1,0)
    return data

    # cols=8
    # for i in range(cols):
    #     plt.subplot(cols,1,(i+1))
    #     plt.plot(data[:,i],label=df.columns[i])
    #     plt.legend(loc='upper right')
    # plt.show()


def split_data(data,train_size):
    x_cols=8
    trainX=data[:train_size,:x_cols]
    trainY=data[:train_size,x_cols]
    testX=data[train_size:,:x_cols]
    testY=data[train_size:,x_cols]
    trainX=trainX.reshape(trainX.shape[0],1,trainX.shape[1])
    testX=testX.reshape(testX.shape[0],1,testX.shape[1])
    return trainX,trainY,testX,testY



def createModel(input_shape):
    model=Sequential()
    model.add(layers.LSTM(50,input_shape=input_shape))
    model.add(layers.Dense(1))
    optimizer=optimizers.Adam(learning_rate=0.01)
    model.compile(optimizer=optimizer,loss='mae')
    return model

data=preprocess()
train_size=365*24
trainX,trainY,testX,testY=split_data(data,train_size)

model=createModel((trainX.shape[1],trainX.shape[2]))

history=model.fit(trainX,trainY,epochs=50,batch_size=72,validation_data=(testX, testY), verbose=2, shuffle=False)

plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()

