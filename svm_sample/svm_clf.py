from sklearn.svm import SVC
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import utils.dataLoader as dataLoader


def getAOC(ypred,y):
    tlabel=1
    flabel=-1
    tIndices=np.argwhere(y==tlabel)
    tp=np.sum(ypred[tIndices]==tlabel)
    fn=len(tIndices)-tp
    fIndices=np.argwhere(y==flabel)
    tn=np.sum(ypred[fIndices]==flabel)
    fp=len(fIndices)-tn
    tpr=tp/(tp+fn)
    fpr=fp/(fp+tn)
    print('{0},{1},{2},{3},tpr={4},fpr={5}'.format(tp,fn,fp,tn,tpr,fpr))

data=dataLoader.loadBreastCancerData()
X=data[:,1:]
Y=data[:,0]
Y=3-Y
# 归一化数据
ms=np.mean(X,axis=0)
ss=np.std(X,axis=0)
X=(X-ms)/ss

indices=np.random.shuffle(np.arange(len(Y)))
testSize=60
X_test=X[:testSize]
Y_test=Y[:testSize]
X_train=X[testSize:]
Y_train=Y[testSize:]
print(Y_test)

# 构建模型
for i in range(21):
    C=np.power(10.0,-5+i)
    print('**************{0}**************'.format(C))
    clf=SVC(C,kernel='rbf',verbose=True)
    clf.fit(X_train,Y_train)
    ypred=clf.predict(X_test)
    
    ratio=np.mean(ypred==Y_test)
    print("precision:",ratio)
    getAOC(ypred,Y_test)

    
    


