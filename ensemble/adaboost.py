import numpy as np
import math
import pandas as pd

# AdaBoost集成分类器模型
class AdaBoost(object):

    def __init__(self):
        self._classifiers=[]
        self._eigenSize=10
        

    def predict(self,dataMat):
        m,n=dataMat.shape
        aggClassEst=np.zeros((m,1))
        for classifier in self._classifiers:
            retLabels=self._classifyItem(dataMat,classifier['threshold'],classifier['eigenIndex'],classifier['inequal'])
            aggClassEst+=classifier['alpha']*retLabels
            print(aggClassEst)
        return np.sign(aggClassEst)
            

    def fit(self,dataMat,vectLabels,iterNum=10):
        # 找出分类错误率最低的特征，特征阈值，
        m,n=dataMat.shape
        weights=np.ones((m,1),dtype=float)/m
        # 累积分类概率
        aggClassEst=np.zeros((m,1))
        for i in range(iterNum):
            bestClassifier,err,retLabels=self._findBestClassifier(dataMat,vectLabels,weights)
            # print("weights:\n",weights)
            # print("retLabels:\n",retLabels)
            alpha=0.5*np.log((1-err)/max(err,1e-16))
            bestClassifier['alpha']=alpha
            self._classifiers.append(bestClassifier)
            # print(retLabels.shape)           
            aggClassEst+=alpha*retLabels
            # print("aggClassEst:\n",aggClassEst[:,-1])

            probs=np.zeros((m,1))
            probs[np.sign(aggClassEst)!=vectLabels]=1
            errorRate=np.sum(probs*np.ones((m,1)))
            print("iteration {0},errorRate={1}:".format((i+1),errorRate/m))
            if(errorRate<=0):
                return
            # 更新权重
            signs=np.ones((m,1))*-1
            signs[retLabels!=vectLabels]=1
            weights=weights*np.exp(signs)
            weights=weights/np.sum(weights)

    
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
    train_count=7
    X_train=data[0:train_count,0:-1]
    Y_train=data[0:train_count,-1:]
    ada=AdaBoost()
    ada.fit(X_train,Y_train)
    # print(Y)
    # print(ada._classifiers)
    X_valid=data[train_count:,0:-1]
    Y_valid=data[train_count:,-1:]
    labelResult=ada.predict(X_valid)
    m=X_valid.shape[0]
    errorRate=np.zeros((m,1))
    errorRate[labelResult!=Y_valid]=1
    print(errorRate)
    print("分类错误率:",np.sum(errorRate)/m)


