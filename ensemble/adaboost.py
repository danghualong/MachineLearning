import numpy as np
import math
import pandas as pd
import pltUtil as util
from sklearn.model_selection import train_test_split,KFold

# AdaBoost集成分类器模型
class AdaBoost(object):

    def __init__(self):
        self._classifiers=[]
        self._eigenSize=10
        # 累积分类结果值
        self.aggClassEst=None
        # 错误率集合
        self.error_rate_results=[]
        

    def predict(self,dataMat):
        m,n=dataMat.shape
        aggClassEst=np.zeros((m,1))
        for classifier in self._classifiers:
            retLabels=self._classifyItem(dataMat,classifier['threshold'],classifier['eigenIndex'],classifier['inequal'])
            aggClassEst+=classifier['alpha']*retLabels
            # print(aggClassEst)
        return aggClassEst
            

    def fit(self,dataMat,vectLabels,iterNum=10):
        # 找出分类错误率最低的特征，特征阈值，
        m,n=dataMat.shape
        weights=np.ones((m,1),dtype=float)/m
        # 累积分类概率
        self.aggClassEst=np.zeros((m,1))
        for i in range(iterNum):
            # 找到最佳的基分类器
            # 计算分类错误率
            bestClassifier,err,retLabels=self._findBestClassifier(dataMat,vectLabels,weights)
            # 求出当前分类器的权重
            alpha=0.5*np.log((1-err)/max(err,1e-16))
            bestClassifier['alpha']=alpha
            # 重新更新样本权重
            self.updateWeights(weights,alpha,retLabels,vectLabels)
            # 计算多个分类器的累加结果(分类错误率看是否有改善)
            self._classifiers.append(bestClassifier)
            self.aggClassEst+=alpha*retLabels
            error_rate=self.get_error_rate(self.aggClassEst,vectLabels)
            self.error_rate_results.append(error_rate)
            

    def updateWeights(self,weights,alpha,predLabels,labels):
        '''
        更新权重
        '''
        m=len(labels)
        signs=np.ones((m,1))*-1
        signs[predLabels!=labels]=1
        weights=weights*np.exp(alpha*signs)
        weights=weights/np.sum(weights)
    
    def get_error_rate(self,predLabels,labels):
        m=len(labels)
        probs=np.zeros((m,1))
        probs[np.sign(predLabels)!=labels]=1
        errorRate=np.mean(probs)
        return errorRate
    
    def _findBestClassifier(self,dataMat,vectLabels,weights):
        m,n=dataMat.shape
        errMin=math.inf
        classifier={}
        bestClassEst=None
        for i in range(n):
            arrs=dataMat[:,i]
            rng_min=min(arrs)
            rng_max=max(arrs)
            step=float(rng_max-rng_min)/self._eigenSize
            for j in range(-1,self._eigenSize+1):
                for inequal in ['lt','gt']:
                    threshold=rng_min+float(j)*step
                    retLabels=self._classifyItem(dataMat,threshold,i,inequal)
                    # 分类错误累加数
                    errs=np.zeros((m,1))
                    errs[retLabels!=vectLabels]=1
                    errVal=np.sum(np.multiply(weights,errs))
                    # print('eigenIndex={0},threshold={1},inequal={2},errVal={3}'.format(i,threshold,inequal,errVal))
                    if(errVal<errMin):
                        errMin=errVal
                        bestClassEst=retLabels
                        classifier['eigenIndex']=i
                        classifier['threshold']=threshold
                        classifier['inequal']=inequal
                        # print(classifier,errMin,bestClassEst,vectLabels[:,-1])
        return classifier,errMin,bestClassEst

    def _classifyItem(self,dataMat,threshold,eigenIndex,inequal):
        m=dataMat.shape[0]
        arrs=dataMat[:,eigenIndex]
        retLabels=np.ones((m,1))
        if(inequal=='lt'):
            retLabels[arrs<=threshold]=-1.0
        else:
            retLabels[arrs>threshold]=-1.0
        return retLabels      
    

if __name__=="__main__":
    origin_data=pd.read_excel('./ensemble/adaboost.csv',sheet_name='Sheet1')
    data=np.array(origin_data,dtype=np.int32)
    print(origin_data.columns)
    X_train,X_test,Y_train,Y_test=train_test_split(data[:,0:-1],data[:,-1:],test_size=0.3,random_state=10)
    print(Y_train.shape[0],Y_test.shape[0])
    ada=AdaBoost()
    ada.fit(X_train,Y_train,500)
    util.draw(ada.error_rate_results,'分类累计错误率')
    util.drawAuc(ada.aggClassEst,Y_train)

    aggClassEst=ada.predict(X_test)
    labelResult=np.sign(aggClassEst)
    m=X_test.shape[0]
    errorRate=np.zeros((m,1))
    errorRate[labelResult!=Y_test]=1
    # print(errorRate)
    print("分类错误率:",np.sum(errorRate)/m)
    util.drawAuc(aggClassEst,Y_test)



