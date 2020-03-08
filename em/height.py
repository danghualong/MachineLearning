import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

np.random.seed(100)

f_avg=1.50
f_std=0.22
f_size=600

m_avg=2.2
m_std=0.20
m_size=400

f_heights=np.random.normal(f_avg,f_std,f_size)
m_heights=np.random.normal(m_avg,m_std,m_size)


def draw():
    bins=20
    n1,bins1,pathes1=plt.hist(f_heights,bins=bins,color='r',alpha=0.5,normed=1)
    n2,bins2,pathes2=plt.hist(m_heights,bins=bins,color='g',alpha=0.8,normed=1)
    y1=norm.pdf(bins1,f_avg,f_std)
    y2=norm.pdf(bins2,m_avg,m_std)
    plt.plot(bins1,y1,'b--')
    plt.plot(bins2,y2,'k-')
    plt.show()

draw()

class EMHeights(object):
    def __init__(self,heights):
        # r=np.random.random()
        self.ratios=np.array([0.5,0.5])
        self.avgs=np.array([1,2])
        self.stds=np.array([0.3,0.3])
        self.heights=heights
        self.gammas=None
        self.lastAvgs=None
        self.total=len(heights)

    @staticmethod
    def gausianP(x,t_avg,t_std):
        return np.exp(-np.power((x-t_avg),2)/(2*t_std*t_std))/(math.sqrt(math.pi*2)*t_std)

    def stepE(self):
        p1s=EMHeights.gausianP(self.heights,self.avgs[0],self.stds[0])*self.ratios[0]
        p2s=EMHeights.gausianP(self.heights,self.avgs[1],self.stds[1])*self.ratios[1]
        return np.array([p1s/(p1s+p2s),p2s/(p1s+p2s)])
    
    def stepM(self):
        self.gammas=self.stepE()
        print(self.gammas)
        tmpSum=np.sum(self.gammas,axis=1)
        self.lastAvgs=np.copy(self.avgs)
        self.ratios=tmpSum/np.sum(tmpSum)
        self.avgs=np.sum(np.multiply(self.gammas,self.heights),axis=1)/tmpSum
        for i in range(2):
            self.stds[i]=np.sqrt(np.sum(np.power((self.heights-self.avgs[0]),2)*self.gammas[i])/tmpSum[i])
        
        print("****ratios*****",self.ratios)
        print("****avgs*****",self.avgs)
        print("****stds*****",self.stds)

    def nodiff(self):
        diff=self.avgs-self.lastAvgs
        for i in range(len(diff)):
            if(abs(diff[i])>1e-8):
                return False
        return True
    
    def calc(self):
        times=10000
        i=0
        while(i<times):
            print('=========',(i+1))
            self.stepM()
            if(self.nodiff()):
                break
            i+=1

heights=np.concatenate((f_heights,m_heights))
print(heights)
obj=EMHeights(heights)
obj.calc()
        



        
    





