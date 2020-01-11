import pandas as pd
import numpy as np
import math
# import os
# dirName=dirName=os.path.dirname(__file__)



class DataNode(object):
    def __init__(self,dataset,labels,featureNames):
        self._dataset=dataset
        self._labels=labels
        self._featureNames=featureNames
        self._childNodes=None
        self._kinds=None
        self._resultLabel=None
        self.nextFeatureName=None

    @property
    def entropy(self):
        return self._entropy
    @entropy.setter
    def entropy(self,val):
        self._entropy=val
    
    @property
    def nextFeatureIndex(self):
        return self._nextFeatureIndex
    @nextFeatureIndex.setter
    def nextFeatureIndex(self,val):
        self._nextFeatureIndex=val
        self.nextFeatureName=self._featureNames[val]
    @property
    def childNodes(self):
        return self._childNodes
    
    @property
    def resultLabel(self):
        return self._resultLabel

    @property
    def kinds(self):
        return self._kinds
    
    def assign(self):
        dictData=DataNode.getCategoryRatios(self._labels)
        featureIndex=DataNode.chooseBestFeature(self._dataset,self._labels)
        # 当前没有特征列
        if(featureIndex==-1):
            sortedDictData=sorted(dictData,key=lambda x:x[1],reverse=True)
            print(sortedDictData)
            self._resultLabel=sortedDictData[0].key
            return
        self.nextFeatureIndex=featureIndex
        self.entropy=DataNode.getEnt(dictData)
        # 当ent为0时,不需要再分隔
        if(self.entropy==0):
            self._resultLabel=self._labels[0]
            return

        # 分割数据
        self._childNodes=[]
        self._kinds=[]
        subDatasetList,subLabelsList,subNames,kinds=DataNode.split_data(self._dataset,self._labels,self._featureNames,featureIndex)
        for i in range(len(subLabelsList)):
            childNode=DataNode(subDatasetList[i],subLabelsList[i],subNames)
            self._childNodes.append(childNode)
            self._kinds.append(kinds[i])

    @staticmethod
    def getCategoryRatios(labels):
        total=len(labels)
        dictData={}
        for label in labels:
            if(label not in dictData):
                dictData[label]=0
            dictData[label]+=1
        for key in dictData.keys():
            dictData[key]/=total
        return dictData
    @staticmethod
    def getEnt(dictData):
        if(dictData==None):
            return 0
        else:
            sum=0
            for key in dictData.keys():
                d=dictData[key]
                # print("d={0},log={1}".format(d,math.log(d,2)))
                sum-=d*math.log(d,2)
            return sum
    @staticmethod
    def getGini(dictData):
        sum=0
        for key in dictData.keys():
            sum+=dictData[key]**2
        return 1-sum
    @staticmethod
    def chooseBestFeature(dataset,labels):
        featureCount=dataset.shape[1]
        if(featureCount==0):
            return -1
        bestFeatureIndex=0
        if(featureCount==1):
            return bestFeatureIndex
        rowCount=len(labels)
        miniEnt=math.inf
        for i in range(featureCount):
            curFeatures=dataset[:,i]
            kinds=set(curFeatures)
            subLabelsList=[]
            for kind in kinds:
                subLabels=labels[curFeatures==kind]
                subLabelsList.append(subLabels)
            sumEnt=0
            for subLabels in subLabelsList:
                p=float(len(subLabels))/rowCount
                ratios=DataNode.getCategoryRatios(subLabels)
                sumEnt+=p*DataNode.getEnt(ratios)
            if(sumEnt<miniEnt):
                miniEnt=sumEnt
                bestFeatureIndex=i
        return bestFeatureIndex
    @staticmethod
    def split_data(dataset,labels,featureNames,featureIndex):
        if(featureIndex<0 or featureIndex>=dataset.shape[1]):
            return
        curFeatures=dataset[:,featureIndex]
        kinds=list(set(curFeatures))
        subLabelsList=[]
        subDatasetList=[]
        for kind in kinds:
            subLabels=labels[curFeatures==kind]
            subDataset=dataset[curFeatures==kind]
            subLabelsList.append(subLabels)
            subDatasetList.append(subDataset)
        for i in range(len(subLabelsList)):
            subDataset=subDatasetList[i]
            subDatasetList[i]=np.concatenate((subDataset[:,0:featureIndex],subDataset[:,featureIndex+1:]),axis=1)
        subNames=np.concatenate((featureNames[0:featureIndex],featureNames[featureIndex+1:]))
        return subDatasetList,subLabelsList,subNames,kinds
    
class DecisionTree(object):
    def __init__(self):
        self._root=None

    def fit(self,dataset,labels,featureNames):
        self._root=DataNode(dataset,labels,featureNames)
        self.showAll(self._root)

    def showAll(self,dataNode):
        if(dataNode!=None):
            dataNode.assign()
            print("featureName={0},kinds={1},ent={2}".format(dataNode.nextFeatureName,dataNode.kinds,dataNode.entropy))
        if(dataNode.childNodes!=None):
            for subNode in dataNode.childNodes:
                self.showAll(subNode)

    def predict(self,case):
        if(self._root==None):
            return
        node=self._root
        while(node!=None):
            key=node.nextFeatureName
            print(key,node._labels)
            if(key not in case.keys()):
                return
            if(node.resultLabel!=None):
                print("The category is:",node.resultLabel)
                return
            if(node.kinds==None):
                return
            index=node.kinds.index(case[key])
            if(index<0):
                return
            
            node=node.childNodes[index]


if __name__=='__main__':
    
    origin_data=pd.read_excel('./decisionTree/dt.csv',sheet_name='Sheet1')
    data=np.array(origin_data,dtype=np.int32)
    print(origin_data.columns)
    X=data[:,0:-1]
    Y=data[:,-1]

    columns=origin_data.columns
    model=DecisionTree()
    model.fit(X,Y,columns)
    model.predict({'天气':0,'温度':0,'湿度':0,'风力':1})
