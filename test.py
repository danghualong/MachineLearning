import numpy as np

arr=np.arange(10)
arr2=arr.reshape((-1,1))
arr3=arr2.flatten()
print(np.dot(arr2.T,arr2))
print(np.multiply(arr2.T,arr2))