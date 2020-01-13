import numpy as np
import matplotlib.pyplot as plt

def drawAuc(aggClassEst,vectLabels):
    m=vectLabels.shape[0]
    posCount=np.sum(vectLabels==1.0)
    # 即实际为阳性数量
    yStep=1.0/posCount
    # 实际为阴性的数量
    xStep=1.0/float(m-posCount)
    # 按照预测强度排序
    tmpClassEst=aggClassEst.reshape(m)
    indices=tmpClassEst.argsort()
    X=[]
    Y=[]
    curX=1
    curY=1
    X.append(curX)
    Y.append(curY)
    # 累计高度,
    aggH=0
    for index in indices:
        # 由真阳性变成假阴性
        if(vectLabels[index]==1):
            curY-=yStep
        # 由假阳性变成真阴性
        else:
            curX-=xStep
            aggH+=curY
        # print(curX,curY)
        X.append(curX)
        Y.append(curY)
    # 面积为area=aggH*xStep
    auc=aggH*xStep
    print("auc-roc is :",auc)
    # 画auc-roc曲线
    plt.plot(X,Y,'b-')
    plt.plot(np.array([0,1]),np.array([0,1]),'g--')
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    plt.title('the auc of the model')
    plt.show()