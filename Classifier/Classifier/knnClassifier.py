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
    sortIndexes=sum.argsort()
    dict={}
    for i in range(k):
        type=labels[sortIndexes[i],0]
        dict[type]=dict.get(type,0)+1
    sortedTypes=sorted(dict.iteritems(),key=lambda i:i[1],reverse=True)
    return dictTypes[int(sortedTypes[0][0])]

if __name__=="__main__":
    mat,labels=loader.loadData(r"samples\result.txt")
    inX=np.array([10,20])
    curType=classify(inX,mat,labels,3)
    print "The type of the film is ",curType

