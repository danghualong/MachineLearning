import numpy as np
import tensorflow as tf
from tensorflow.keras import layers,models


np.random.seed(10)

data=np.random.normal(size=(2,3,4))
# print(data)

inputLayer=layers.Input(shape=(3,4))
lstm1=layers.LSTM(6,return_sequences=False,return_state=True)(inputLayer)

model=models.Model(inputs=inputLayer,outputs=(lstm1))
outputs,lastHiddenState,lastCellState=model.predict(data)
print('\nHidden States')
print(outputs) #当return_sequences为true时，返回所有时序的Hidden State,反之，返回最后一个时序的Hidden State
print('\nLast Hidden State')
print(lastHiddenState) #当return_state为true时，返回最后一个时序的Hidden State 和 Cell State

print('\nLast Cell State')
print(lastCellState)


