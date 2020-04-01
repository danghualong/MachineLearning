import numpy as np

data=np.array([[1.0,2.0,3.0],[2,3.9,6.1],[3,6.01,9.03],[4,8.01,12.04]])
u,sigma,vT=np.linalg.svd(data)
print(u)
print(sigma)
print(vT)
k=1
u2=u[:,:k]
sigma2=np.diag(sigma[:k])
vT2=vT[:k,:]
data2=u2.dot(sigma2).dot(vT2)
print(data)
print(data2)

