import numpy as np
import random
import matplotlib.pyplot as plt

#直观体验中心极限定理

SAMPLE_SIZE=36
SAMPLE_NUMS=100

def getSample(data):
    sample=[]
    for i in range(SAMPLE_SIZE):
        sample.append(data[int(random.random()*len(data))])
    return sample

def getSampleStat(data):
    means=[]
    for i in range(SAMPLE_NUMS):
        sample=getSample(data)
        arr=np.array(sample)
        means.append(arr.mean())
    return np.array(means)

def draw(data,xlabel=None,ylabel=None,title=None):
    bins=int(SAMPLE_NUMS/5);
    plt.hist(data,bins=bins,density=0,facecolor='r',edgecolor='b',orientation='vertical')
    if(xlabel!=None):
        plt.xlabel(xlabel)
    if(ylabel!=None):
        plt.ylabel(ylabel)
    if(title!=None):
        plt.title(title)
    plt.show()


if __name__=='__main__':
    data=np.random.randint(1,7,10000)
    print('总体均值:',data.mean())
    std1=data.std()
    print('总体标准差:{0:.4f}'.format(std1))
    meanSamples=getSampleStat(data)
    std2=meanSamples.std()
    print('样本均值:mean={0}，std={1}'.format(meanSamples.mean(),std2))
    print('sqrt({0})={2},std1/std2={1}'.format(SAMPLE_SIZE,std1/std2,np.sqrt(SAMPLE_SIZE)))
    draw(meanSamples,'X','Freq')
    



