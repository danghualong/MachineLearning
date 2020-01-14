import pandas as pd
import numpy as np

def loadIrisData():
    data=pd.read_csv('./utils/data/iris.data',header=None,names=['x1','x2','x3','x4','y'])
    class_mapping={'Iris-virginica':2,'Iris-versicolor':1,'Iris-setosa':0}
    data.iloc[:,4]=data.iloc[:,4].map(class_mapping)
    return np.array(data)

def loadCityData():
    data=pd.read_csv('./utils/data/city.csv',header=None,sep=',')
    return np.array(data) 