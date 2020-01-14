# encoding=utf-8

import numpy as np
import dataLoader as loader
import urllib

dictTypes={0:u"爱情片",1:u"动作片"}

def classify(inX,mat,labels,k):
    mat=inX-mat
    mat=mat**2
    sum= mat.sum(axis=1)
    sum=sum**0.5
    sortIndices=sum.argsort()
    dict={}
    for i in range(k):
        type=labels[sortIndices[i]]
        dict[type]=dict.get(type,0)+1
    print(dict)
    sortedTypes=sorted(dict,key=lambda i:i[0],reverse=True)
    return dictTypes[int(sortedTypes[0][0])]

if __name__=="__main__":
    mat,labels=loader.loadData("./Classifier/Classifier/samples/result.txt")
    X=np.array(mat)[:,1:]
    Y=np.array(labels)
    inX=np.array([[30,20]])
    curType=classify(inX,X,Y,3)
    print("The type of the film is ",curType)

