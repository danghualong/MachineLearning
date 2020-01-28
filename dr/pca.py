import numpy as np

def pca(dataset,redDim):
    meanvect=np.mean(dataset,axis=0)
    removedDataset=dataset-meanvect
    # 计算协方差矩阵
    covmat=np.cov(removedDataset,rowvar=False)
    print(covmat)
    # 特征值分解
    eigvals,eigvects=np.linalg.eig(covmat)
    # 选择前redDim个特征向量
    indvals=np.argsort(eigvals)
    indvals=indvals[:-(redDim+1):-1]
    redeigvects=eigvects[:,indvals]
    print(redeigvects)
    lowDimMat=np.dot(removedDataset,redeigvects)
    reconMat=np.dot(lowDimMat,redeigvects.T)+meanvect
    return lowDimMat,reconMat


dataset=np.array([[1.0,2.0,3.0],[2,3.9,6.1],[3,6.01,9.03],[4,8.01,12.04]])
lowDimMat,reconMat=pca(dataset,1)
print(lowDimMat)
print(reconMat)



