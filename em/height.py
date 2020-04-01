import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

np.random.seed(100)

f_avg=1.59
f_std=0.12
f_size=600

m_avg=1.78
m_std=0.15
m_size=400

f_heights=np.random.normal(f_avg,f_std,f_size)
m_heights=np.random.normal(m_avg,m_std,m_size)


def draw():
    bins=20
    n1,bins1,pathes1=plt.hist(f_heights,bins=bins,color='r',alpha=0.5,density=1)
    n2,bins2,pathes2=plt.hist(m_heights,bins=bins,color='g',alpha=0.8,density=1)
    y1=norm.pdf(bins1,f_avg,f_std)
    y2=norm.pdf(bins2,m_avg,m_std)
    plt.plot(bins1,y1,'b--')
    plt.plot(bins2,y2,'k-')
    plt.show()



class EMHeights(object):
    def __init__(self,heights):
        # r=np.random.random()
        self.alphas=np.array([0.6,0.4])
        self.avgs=np.array([1.4,1.9])
        self.stds=np.array([0.12,0.15])
        self.count=len(self.alphas)
        self.heights=heights
        self.gammas=None
        self.lastAvgs=None
        self.lastStds=None
        self.total=len(heights)

    def stepE(self):
        # 获取每个点隶属于每个分布的概率
        p1s=norm.pdf(self.heights,loc=self.avgs[0],scale=self.stds[0])
        p2s=norm.pdf(self.heights,loc=self.avgs[1],scale=self.stds[1])
        # p1s*=self.alphas[0]
        # p2s*=self.alphas[1]
        return np.array([p1s/(p1s+p2s),p2s/(p1s+p2s)])
    
    def stepM(self):
        self.gammas=self.stepE()
        # print(self.gammas.shape)
        tmpSum=np.sum(self.gammas,axis=1)
        # print(tmpSum)
        # memory the last averages
        self.lastAvgs=np.copy(self.avgs)
        self.lastStds=np.copy(self.stds)
        # 每个分布所占比例alpha
        self.alphas=tmpSum/np.sum(tmpSum)
        # 计算每个分布的u
        self.avgs=np.sum(np.multiply(self.gammas,self.heights),axis=1)/tmpSum
        # 计算每个分布的std
        for i in range(self.count):
            self.stds[i]=np.sqrt(np.sum(np.power((self.heights-self.avgs[0]),2)*self.gammas[i])/tmpSum[i])
        
        print("****alphas*****",self.alphas)
        print("****avgs*****",self.avgs)
        print("****stds*****",self.stds)

    def converged(self):
        diff=self.stds-self.lastStds
        print(diff)
        return np.abs(np.sum(diff))<1e-4
        # for i in range(len(diff)):
        #     if(abs(diff[i])>1e-8):
        #         return False
        # return True
    
    def calc(self):
        times=10000
        i=0
        while(i<times):
            print('=========',(i+1))
            self.stepM()
            if(self.converged()):
                break
            i+=1

# draw()
heights=np.concatenate((f_heights,m_heights))
obj=EMHeights(heights)
obj.calc()
        



        
    





