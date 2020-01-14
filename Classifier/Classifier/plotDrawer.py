from matplotlib import pyplot as plt
import numpy as np
import dataLoader as loader


def draw(mat):
    arrX=mat[:,0]
    arrY=mat[:,1]
    plt.figure(figsize=(12,8))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(arrX,arrY)
    plt.show()

def drawBar():
    n=8
    vecX=np.arange(n)+0.85
    vecY=np.random.uniform(0,1,n)
    plt.xlim(0,n+1)
    plt.ylim(0,1.2)
    plt.bar(vecX,vecY,width=0.3,facecolor='green')
    for x,y in zip(vecX,vecY):
        plt.text(x+0.2,y+0.05,'%.2f'%y,va='center',ha='center')
    plt.show()


def drawScatter(vecX,vecY,types,**labels):
    xMax=float(max(vecX))
    xMin=float(min(vecX))
    yMax=float(max(vecY))
    yMin=float(min(vecY))
    plt.xlim(xMin-0.1,xMax+0.1)
    plt.ylim(yMin-0.1,yMax+0.1)

    uniqTypes=set(types)
    dictTypes={}
    for type in uniqTypes:
        dictTypes[type]=[[],[]]
    for i in range(len(types)):
        dictTypes[types[i]][0].append(vecX[i])
        dictTypes[types[i]][1].append(vecY[i])
    for type in uniqTypes:
        plt.scatter(dictTypes[type][0],dictTypes[type][1],s=50)
    plt.show()


if __name__=="__main__":
    mat,types=loader.loadData("./Classifier/Classifier/samples\data1.txt")
    mat=np.mat(mat)
    vecX=mat[:,0]
    vecY=mat[:,1]
    drawScatter(vecX,vecY,types)
