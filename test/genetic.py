import random
from functools import reduce
import numpy as np

class PopulationItem(object):
    def __init__(self):
        self.series=[]
        self.weight=0
        self.price=0
    
    def getRatio(self,totalWeight):
        if(totalWeight<=0):
            return 0
        return float(self.weight)/totalWeight

class Genetic(object):
    def __init__(self,weights,prices,max_weight,variation_rate=0.05,sample_size=10):
        self._weights=np.array(weights)
        self._prices=np.array(prices)
        self._maxWeight=max_weight
        self._variation_rate=variation_rate
        self._sample_size=sample_size
        self._goods_count=len(weights)
        self.populations=[]
        self.totalPrices=0
        self.bestItem=None

    # 初始化种群
    def initPopulation(self):
        for i in range(self._sample_size):
            item={}
            tmpArr=np.zeros((self._goods_count))
            randoms=np.random.random(self._goods_count)
            tmpArr[randoms>0.5]=1
            item['series']=tmpArr
            self.populations.append(item)
        # 计算种群个体的性状值
        self.cal(self.populations)
        return self.populations
    # 自然选择
    def naturalSelect(self):
        # 淘汰当前世代中不适宜的物种
        leaveout=list(filter(lambda x:x['weight']<=self._maxWeight,self.populations))
        # 标注当前世代的最适宜个体（即价格最大个体)
        totalWeight,curMaxPrice=self.getBestIndividual(leaveout)
        # 选择能繁殖后代的个体
        parents=Genetic.selectParents(leaveout,self._sample_size,totalWeight)
        return parents
    # 标注当前世代的最适宜个体（即价格最大个体)
    def getBestIndividual(self,items):
        totalWeight=0
        curMaxPrice=0
        for item in items:
            totalWeight+=item['weight']
            if(curMaxPrice<item['price']):
                curMaxPrice=item['price']
            if(self.bestItem==None):
                self.bestItem=item
            if(self.bestItem['price']<item['price']):
                self.bestItem=item
        # print("curPrice={0},maxPrice={1}".format(curMaxPrice,self.bestItem['price']))
        return totalWeight,curMaxPrice
    # 杂交繁殖
    def crossover(self,parents):
        # 两两杂交
        descents=[]
        for i in range(0,len(parents),2):
           sepIndex=random.randint(1,self._goods_count-1)
           descents.append(parents[i].copy())
           descents.append(parents[i+1].copy())
           series1=descents[i]['series']
           series2=descents[i+1]['series']
           sec1=descents[i]['series'][sepIndex:]
           sec2=descents[i+1]['series'][sepIndex:]
           descents[i]['series']=np.concatenate((series1[:sepIndex],series2[sepIndex:]))
           descents[i+1]['series']=np.concatenate((series2[:sepIndex],series1[sepIndex:]))
        # 增加基因变异
        self.variation(descents)
        # 产生新的种群
        self.populations=descents
        # 计算种群个体的性状值
        self.cal(self.populations)
        return descents
    # 增加基因变异
    def variation(self,items):
        for item in items:
            randoms=np.random.random((self._goods_count))
            indices=np.argwhere(randoms<self._variation_rate)
            # print("pre:",item['series'])
            item['series'][indices]=1-item['series'][indices]
            # print("post:",item['series'])      
    # 计算种群个体的性状值    
    def cal(self,items):
        for i in range(len(items)):
           series=items[i]['series']
           items[i]['weight']=np.sum(self._weights[series==1])
           items[i]['price']=np.sum(self._prices[series==1])
    # 选择能繁殖后代的个体
    @staticmethod   
    def selectParents(items,sampleSize,totalWeight):
        parents=[]
        for i in range(sampleSize):
            rndWeight=random.random()*totalWeight
            cumWeight=0
            for k in items:
                cumWeight+=k['price']
                if(rndWeight<cumWeight):
                    parents.append(k)
                    break
        return parents
        
        

if __name__=="__main__":
    weights=(10,15,20,25,30,35)
    prices=(15,25,35,45,55,70)
    maxWeight=85
    gene=Genetic(weights,prices,maxWeight)
    result=gene.initPopulation()
    # print(result)
    n=0
    while n<100:
        parents=gene.naturalSelect()
        # print("优胜劣汰:",parents)
        children=gene.crossover(parents)
        # print("繁殖:",children)
        n+=1
    print("bestItem={0}".format(gene.bestItem))


                 

