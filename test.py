import numpy as np

mat=np.arange(6).reshape((2,3))
print(mat)

vect=np.array([0,1,2])

res=np.multiply(mat,vect)

res2=np.dot(mat,vect.T)
print(res)
print(res2.T.shape)


