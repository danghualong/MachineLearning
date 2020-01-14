import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from utils.dataLoader import loadIrisData

def testPCA():
    data=loadIrisData()
    X=data[:,:-1]
    pca=PCA(n_components='mle',svd_solver='auto')
    pca.fit(X)
    reduceX=pca.transform(X)
    print('降维后的方差占总方差比例:',pca.explained_variance_ratio_)
    print('降维后的特征数:',pca.n_components_)
    print('reduceX:',reduceX)

def testLinear():
    pass


