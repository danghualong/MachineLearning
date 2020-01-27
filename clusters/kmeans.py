import numpy as np
import tensorflow as tf
import math

class KMeans(object):
    def __init__(self,dataset):
        self._dataset=dataset

    @staticmethod
    def getDist(inputData,clusters):
        m=clusters.shape[0]
        minDistance=np.inf
        classIndex=-1
        for i in range(m):
            # 计算欧氏距离
            distance=np.sum(np.power(inputData-clusters[i],2))
            if(distance<minDistance):
                minDistance=distance
                classIndex=i
        return classIndex,minDistance
    @staticmethod
    def classify(dataset,clusters):
        '''
        将数据集分派到指定的簇中
        '''
        result=[]
        for i in range(len(dataset)):
            inputData=dataset[i]
            classIndex,distance=KMeans.getDist(inputData,clusters)
            result.append((classIndex,distance))
        return np.array(result)
    @staticmethod
    def isSame(vectA,vectB):
        '''
        判断两个向量数据是否相同
        '''
        count=np.sum(np.equal(vectA,vectB))
        total=len(vectA)
        return count==total

    # 初始化簇
    def initClusters(self,num):
        m,n=self._dataset.shape
        size=math.ceil(m/num)
        clusters=np.zeros((num,n))
        for i in range(num):
            stop=min((i+1)*size,m)
            if(i*size<stop):
                clusters[i]=np.mean(self._dataset[i*size:stop,:],axis=0)
        return clusters
    # 根据各个簇重新调整簇中心
    def regulateClusterCenter(self,classes,clusters):
        num=len(clusters)
        for i in range(num):
            t=np.argwhere(classes[:,0]==i)
            sumLen=t.shape[0]
            if(sumLen>0):
                t=np.reshape(t,(sumLen))
                clusters[i]=np.mean(self._dataset[t],axis=0)
    # 分割数据集到指定簇数量
    def splitData(self,num):
        '''
        分割数据集到指定簇数量
        '''
        m,n=self._dataset.shape
        # 初始化簇
        clusters=self.initClusters(num)
        # 初始化分类
        lastClasses=np.zeros((m,2))
        times=0
        while(times<100):
            # 根据当前簇，重新分类
            classes=KMeans.classify(self._dataset,clusters)
            # print("classes:",self._dataset,classes)
            # 根据各个簇重新调整簇中心
            self.regulateClusterCenter(classes,clusters)
            # 当前分类与上次分类是否一样，如果一样，则停止聚类
            isSame=KMeans.isSame(classes[:,0],lastClasses[:,0])
            lastClasses=classes.copy()
            if(isSame):
                break
            times+=1
            if(times%100==0):
                print('times:',times)
        return lastClasses
# 利用二分法分割数据集，直至分到指定簇数量
def biKmeans(dataset,classes,clusterNum):
    '''
    利用二分法分割数据集，直至分到指定簇数量
    '''
    count=1
    while(count<clusterNum):
        # 当前簇的数量
        curNum=len(set(classes[:,0]))
        #最小误差平方和
        minSSE=np.inf
        # 下一个要进行分类的簇索引
        blockIndex=-1
        # 下一个簇的分类结果
        subClasses=None
        for i in range(curNum):
            # 遍历每一个簇
            subDataset=dataset[classes[:,0]==i]
            if(len(subDataset)<=0):
                continue
            # 对该簇分成2个簇
            obj=KMeans(subDataset)
            splitedClasses=obj.splitData(2)
            # print("splitedclasses",splitedClasses)
            # 其余未进行分类的簇的误差平方和
            sse1=np.sum(classes[classes[:,0]!=i][:,1])
            # 当前一分为二的2个簇的误差均方和
            sse2=np.sum(splitedClasses[:,1])
            # 找到误差最小的分类簇
            if(sse1+sse2<minSSE):
                minSSE=sse1+sse2
                blockIndex=i
                subClasses=splitedClasses
        indices=np.nonzero(classes[:,0]==blockIndex)
        indices2=np.nonzero(subClasses[:,0]==1)
        # print("blockIndex,indices,indices2",blockIndex,indices,indices2)
        # 将新分类的簇中，所有类别为1的改为当前簇的最大索引
        for j in indices2[0]:
            classes[indices[0][j]][0]=count
        # 将当前2个新簇中的误差更新为最新的误差
        for j in range(len(subClasses)):
            classes[indices[0][j]][1]=subClasses[j][1]
        count+=1
        # print("*****after classes:",classes)


np.random.seed(14)
dataset=np.random.standard_normal((12,2))
import matplotlib.pyplot as plt

plt.scatter(dataset[:,0],dataset[:,1])
plt.show()

obj=KMeans(dataset)
classes=obj.splitData(4)
print("Kmeans result:",classes)
print("sse of kmeans:",np.sum(classes[:,1]))

biClasses=np.zeros((len(dataset),2))
biKmeans(dataset,biClasses,4)
print(biClasses)
print("sse of biKmeans:",np.sum(biClasses[:,1]))





            