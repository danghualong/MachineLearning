import numpy as np

# A=UΣV'  AA'=UΣΣ'U'=UDU'  A'A=VΣ'ΣV'=VDV'
# 其中D=ΣΣ'
# 相当于 
# AA'进行特征值分解，特征向量U 特征值ΣΣ'
# A'A进行特征值分解，特征向量V 特征值ΣΣ'
def svd4mat(mat):
    eigVals,eigVects=np.linalg.eig(mat)
    # 按照特征值大小倒序排列
    eigIndices1=np.argsort(eigVals)[::-1]
    eigVals=eigVals[eigIndices1]
    # 开平方为特征值
    sigma=np.sqrt(eigVals)
    # 重新排列特征向量
    reconVects=eigVects[:,eigIndices1]
    return sigma,reconVects
def svd(data):
    m,n=data.shape
    data=data/255
    sigma1,U=svd4mat(np.dot(data,data.T))
    sigma2,V=svd4mat(np.dot(data.T,data))
    sigma=sigma2 if m>n else sigma1
    sigma=sigma*255
    return U,sigma,V.T

# 方法2:
# U=A*Inv(ΣV') ===> U=AV*Inv(Σ)
# V'=Inv(UΣ)*A ===> V'=Inv(Σ)*U'A
def mysvd_u(data):
    m,n=data.shape
    mat=np.dot(data,data.T)
    eigVals,eigVects=np.linalg.eig(mat)
    # print(eigVals,eigVects)
    eigValIndices=np.argsort(eigVals)[::-1]
    # print(eigValIndices)
    eigVals=eigVals[eigValIndices]
    # print(eigVals)
    U=eigVects[:,eigValIndices]
    sigma=np.sqrt(eigVals)
    diag=np.diag(sigma)
    sigmaInv=np.linalg.inv(diag)
    VT=sigmaInv.dot(U.T).dot(data)
    return U,sigma[:n],VT[:,:n]
def mysvd_v(data):
    m,n=data.shape
    mat=np.dot(data.T,data)
    eigVals,eigVects=np.linalg.eig(mat)
    # print(eigVals,eigVects)
    eigValIndices=np.argsort(eigVals)[::-1]
    # print(eigValIndices)
    eigVals=eigVals[eigValIndices]
    # print(eigVals)
    V=eigVects[:,eigValIndices]
    sigma=np.sqrt(eigVals)
    diag=np.diag(sigma)
    sigmaInv=np.linalg.inv(diag)
    U=data.dot(V).dot(sigmaInv)
    VT=V.T
    return U[:,:m],sigma[:m],VT
def mysvd(data):
    m,n=data.shape
    data=float(data)/255
    if(m>=n):
        U,sigma,VT=mysvd_u(data)
    else:
        U,sigma,VT=mysvd_v(data)
    sigma=int(sigma*255)
    return sigma

if __name__=="__main__":
    dataset=np.array([[1.0,2.0,4.0],[2,12,6.1],[3,31,6.03],[4,-2,12.04]])
    print("from my svd:")
    u,sigma,vT=svd(dataset)
    print('u:',u)
    print("sigma",sigma)
    print('v:',vT)

    u,sigma,vT=svd(dataset.T)
    print('u:',u)
    print("sigma",sigma)
    print('v:',vT)

    print("\rfrom linalg svd:")

    u,sigma,vT=np.linalg.svd(dataset)
    print('u:',u)
    print("sigma",sigma)
    print('v:',vT)

    u,sigma,vT=np.linalg.svd(dataset.T)

    print('u:',u)
    print("sigma",sigma)
    print('v:',vT)

    print("\r测试公式:")
    u,sigma,vT=np.linalg.svd(dataset)
    sigmasquare=np.power(sigma,2)
    total=np.sum(sigmasquare)
    ratio=0
    for i in range(len(sigmasquare)):
        ratio+=sigmasquare[i]/total
        print(ratio)

    A=u[:,:1].dot(np.diag(sigma[:1])).dot(vT[:1,:])
    print(A)

    import matplotlib.pyplot as plt

    # plt.figure()
    plt.scatter(dataset[:,0],dataset[:,2],marker='^')
    plt.scatter(A[:,0],A[:,2],marker='o')

    plt.show()


    



