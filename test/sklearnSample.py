import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
from utils.dataLoader import loadIrisData,loadCityData
import matplotlib.pyplot as plt


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

def testCluster():
    data=loadCityData()
    clusterCount=6
    markers=['*','^','o','s','+','x']
    X=data[:,1:]
    clf=AgglomerativeClustering(n_clusters=clusterCount,linkage='ward')
    clf.fit(X)
    print(clf.labels_)
    draw(X,clf.labels_,clusterCount,markers)
def draw(data,labels,clusters,markers):
    for i in range(clusters):
        members=labels==i
        plt.scatter(data[members,0],data[members,1],marker=markers[i],alpha=.4)
    plt.xlabel('经度')
    plt.ylabel('纬度')
    plt.show()    


if __name__=='__main__':
    testCluster()


