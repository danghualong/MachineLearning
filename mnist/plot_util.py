import matplotlib.pyplot as plt

def plotHistory(history):
    if(history==None):
        return
    plt.plot(history.epoch,history.history.get('accuracy'),label='accuracy')
    plt.plot(history.epoch,history.history.get('val_accuracy'),label='val_accuracy')
    plt.legend(loc='upper left')
    plt.show()

def drawSamples(images):
    for i in range(12):
        plt.subplot(3,4,(i+1))
        plt.xticks([])
        plt.yticks([])
        plt.imshow(images[i])
        plt.grid(False)
    plt.show()