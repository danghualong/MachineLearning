import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
X=np.arange(-100,100)
Y=stats.norm.pdf(X,0,5)
Y2=stats.norm.pdf(X,0,20)

plt.plot(X,Y,color='green')
plt.plot(X,Y2,color='blue')
plt.xlabel('个数')
plt.ylabel('%')
plt.title("正态分布")
plt.show()

