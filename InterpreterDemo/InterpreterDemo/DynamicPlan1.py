# encoding=utf-8
import numpy as np


def calMinCoinCounts(n,coinTypes):
    coins=[0]
    for i in range(n):
        lastMins=[]
        for t in coinTypes:
            if i>=t:
               lastMins.append(coins[i-t])
        if len(lastMins)>0:
            coins.append(min(lastMins)+1)
    return coins;

def getWinProbability(p,times):
    '''n:the times to compete  
       p:the probability of the first team to win the game'''
    #7 win 4 ,5 win 3,4 win 3
    n=times+1 if times%2!=0 else times+2
    n/=2
    ps=np.zeros(pow(n+1,2)).reshape(n+1,n+1)
    for i in range(n+1):
        for j in range(n+1):
            if i==0 and j==0:
                ps[i][j]=1
            elif (i+j)<=times:
                tmp=0
                if i>0:
                    tmp+=ps[i-1][j]*p
                if j>0:
                    tmp+=ps[i][j-1]*(1-p)
                ps[i][j]=tmp
    return ps

def move(n,sI,mI,eI):
    if n==1:
        print '%s--%d-->%s' %(sI,n,eI)
    else:
        move(n-1,sI,eI,mI)
        print '%s--%d-->%s' %(sI,n,eI)
        move(n-1,mI,sI,eI) 

def getPaths(m,n,points):
    '''  '''
    paths=np.zeros(m*n).reshape(m,n)
    paths.dtype='int64'
    for i in range(m):
        for j in range(n):
            if i==0  or j==0:
                paths[i][j]=1
            else:
                tmp=0
                if(i>0):
                    tmp+=paths[i-1][j]
                if j>0:
                    tmp+=paths[i][j-1]
                paths[i][j]=int(tmp)
            for point in points:
                if point[0]==i and point[1]==j:
                    paths[i][j]=0
                    break
    return paths

def C(tmp,arrA,n,m):
    for i in range(m,n+1):
        tmp[m-1]=arrA[i-1]
        if m>1:
            C(tmp,arrA,i-1,m-1)
        else:
            print ','.join(tmp)
            




if __name__=="__main__":
    #points=[[1,2],[1,4],[2,1],[2,5],[4,1],[4,5],[5,2],[5,4]]
    #paths=getPaths(7,8,points)
    #print paths

    arrA=['A','B','C','D','F']
    tmp=['','','']
    C(tmp,arrA,5,3)