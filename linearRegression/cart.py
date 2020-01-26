import pandas as pd
import numpy as np
import math

# import os
# dirName=dirName=os.path.dirname(__file__)



class DataNode(object):
    def __init__(self,featIndex,splitValue,leftNode,rightNode):
        self._featIndex=featIndex
        self._splitValue=splitValue
        self._leftNode=leftNode
        self._rightNode=rightNode

    @property
    def featIndex(self):
        return self._featIndex
    @property
    def leftNode(self):
        return self._leftNode
    @property
    def rightNode(self):
        return self._rightNode
    @property
    def splitValue(self):
        return self._splitValue
        
    def __repr__(self):
        return "{{featIndex:{0},splitValue:{1},leftNode:{2},rightNode:{3}}}".format(self._featIndex,self._splitValue,self.leftNode,self.rightNode)


def getLeafValue(x,labels):
    return np.mean(labels)

def getErrors(x,labels):
    return np.var(labels)*len(labels)

def getEvalFunc(model,testX):
    return model

def linearSolve(x,y):
    xTx=np.dot(x.T,x)
    if(np.linalg.det(xTx)==0):
        raise NameError("the xTx is a singular matrix")
    ws=np.linalg.inv(xTx)@x.T@y
    return ws

def getModelErrors(x,labels):
    ws=linearSolve(x,labels)
    yhat=x@ws
    return np.sum(np.power(yhat-labels,2))
def getModelLeafValue(x,labels):
    return linearSolve(x,labels)
def getModelEvalFunc(model,testX):
    return testX@model

class CartTree(object):
    @staticmethod
    def chooseBestFeature(data,errorFunc=getErrors,splitValueFunc=getLeafValue,minSizeInGroup=1,errorThreshold=1):
        labels=data[:,-1]
        dataset=data[:,:-1]
        featureCount=dataset.shape[1]
        if(featureCount<=0):
            print('no feature to split')
            return None,None
        if(len(set(labels))==1):
            return None,splitValueFunc(dataset,labels)
        totalError=errorFunc(dataset,labels)
        minError=np.inf
        featIndex=0
        splitValue=None
        for i in range(featureCount):
            curFeatures=dataset[:,i]
            kinds=set(curFeatures)
            # 当前特征中的每个值
            for kind in kinds:
                subset1=dataset[dataset[:,i]>=kind]
                subset2=dataset[dataset[:,i]<kind]
                subY1=labels[dataset[:,i]>=kind]
                subY2=labels[dataset[:,i]<kind]
                # 每个子组数量小于组最小容量
                if(subset1.shape[0]<minSizeInGroup or subset2.shape[0]<minSizeInGroup):
                    continue
                try:
                    sumError=errorFunc(subset1,subY1)+errorFunc(subset2,subY2)
                    if(sumError<minError):
                        minError=sumError
                        featIndex=i
                        splitValue=kind
                except NameError as err:
                    continue
                # print("i={0},kind={1},sumErrors={2},minError={3}".format(i,kind,sumError,minError))
        # 当比上次误差减少不超过一定阈值时,无需再划分
        if(totalError-minError<errorThreshold):
            return None,splitValueFunc(dataset,labels)       
        return featIndex,splitValue
    @staticmethod
    def split_data(data,featureIndex,splitValue):
        if(featureIndex==None):
            return None,None
        indices1=data[:,featureIndex]>=splitValue
        indices2=data[:,featureIndex]<splitValue
        subdata1=data[indices1]
        subdata2=data[indices2]
        return subdata1,subdata2
    @staticmethod
    def createTree(data,errorFunc=getErrors,splitValueFunc=getLeafValue,minSizeInGroup=1,errorThreshold=1):
        featIndex,splitValue=CartTree.chooseBestFeature(data,errorFunc,splitValueFunc)
        if(featIndex==None):
            return splitValue
        leftData,rightData=CartTree.split_data(data,featIndex,splitValue)
        leftTree=CartTree.createTree(leftData,errorFunc,splitValueFunc,minSizeInGroup,errorThreshold)
        rightTree=CartTree.createTree(rightData,errorFunc,splitValueFunc,minSizeInGroup,errorThreshold)                                          
        node=DataNode(featIndex,splitValue,leftTree,rightTree)
        return node
    @staticmethod
    def evaluate(tree,testX,evalFunc=getEvalFunc):
        m=testX.shape[0]
        yhats=[]
        for i in range(m):
            yhat=CartTree.evaluateItem(tree,testX[i],evalFunc)
            yhats.append(yhat)
        return yhats
    @staticmethod
    def evaluateItem(tree,oneItem,evalFunc):
        if type(tree).__name__!='DataNode':
            return evalFunc(tree,oneItem)
        if(oneItem[tree.featIndex]>=tree.splitValue):
            return CartTree.evaluateItem(tree.leftNode,oneItem,evalFunc)
        else:
            return CartTree.evaluateItem(tree.rightNode,oneItem,evalFunc)
    @staticmethod
    def linearSolve(data):
        x=data[:,:-1]
        y=data[:,-1]
        return linearSolve(x,y)
        
    

if __name__=='__main__':
    x1=np.arange(1,6,0.1)
    x2=np.arange(3,8,0.1)
    y=x1*5+4*x2
    data=np.vstack((x1,x2,y)).T
    tree=CartTree.createTree(data,errorFunc=getModelErrors,splitValueFunc=getModelLeafValue,minSizeInGroup=2,errorThreshold=0.1)
    print(tree)
    # 求预测值y
    testData=np.array([[1.9,3.9,25.1],[2,4,26],[2.1,4.1,26.9],[2.2,3.9,26.0]])
    yhats=CartTree.evaluate(tree,testData[:,:-1],evalFunc=getModelEvalFunc)
    print(yhats)
    # 求相关系数
    coff=np.corrcoef(testData[:,-1],yhats,rowvar=0)
    print(coff)

    




