import matplotlib.pyplot as plt
import numpy as np

def showTrendency(train_accurs,valid_accurs):
    plt.plot(np.arange(len(train_accurs)),train_accurs,color='r',label='train')
    plt.plot(np.arange(len(valid_accurs)),valid_accurs,color='g',label='valid')
    plt.legend()
    plt.show()

def showOneTrendency(valid_accurs):
    plt.plot(np.arange(len(valid_accurs)),valid_accurs,color='g',label='valid')
    plt.legend()
    plt.show()

def showTrendencies(accurs):
    n=len(accurs)
    for i in range(n):
        subAccurs=accurs[i]
        ax=plt.subplot(n,1,(i+1))
        ax.set_title(subAccurs['lr'])
        train_accurs=subAccurs['train_accurs']
        valid_accurs=subAccurs['test_accurs']
        plt.plot(np.arange(len(train_accurs)),train_accurs,color='r',label='train')
        plt.plot(np.arange(len(valid_accurs)),valid_accurs,color='g',label='valid')
        plt.legend()
    plt.show()
