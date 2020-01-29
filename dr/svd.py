import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import matplotlib.image as pimg
import dr.mysvd as mydr
# from sklearn import datasets
import time
from skimage import io
import os
dirName=dirName=os.path.dirname(__file__)


def getImgAsMatFromFile(filename):
    img=pimg.imread(filename)
    # print(img.shape)
    return img


def plotImg2(*args):
    fig=plt.figure(figsize=(16,9))     
    for i in range(len(args)):
        ax=fig.add_subplot(3,3,(2*i+1))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title('{0} eigens'.format(args[i][0]))
        ax.imshow(args[i][1].astype(np.uint8))
    plt.show()

def recoverBySVD(imgMat, k):
    img_tmp=imgMat.reshape(1440,1080*3)
    # singular value decomposition
    # start1=time.time()
    # U, s, VT = mydr.svd(img_tmp)
    # stop1=time.time()
    # print("mysvd time:{0}".format(stop1-start1))
    start2=time.time()
    U, s, VT = np.linalg.svd(img_tmp)
    stop2=time.time()
    print("linalg.svd time:{0}".format(stop2-start2))
    # choose top k important singular values (or eigens)
    Uk = U[:, 0:k]
    #SK:二维数组
    Sk = np.diag(s[0:k])
    Vk = VT[0:k, :]
    # recover the image
    imgMat_new = Uk.dot(Sk).dot(Vk)
    return imgMat_new.reshape(1440,1080,3)


# -------------------- main --------------------- #
#A = getImgAsMat(0)
#plotImg(A)
#A_new = recoverBySVD(A, 20)
#plotImg(A_new)
if __name__=="__main__":
    A = getImgAsMatFromFile('./dr/data/niu.jpg')
    A_new30 = recoverBySVD(A, 30)
    A_new50 = recoverBySVD(A, 50)
    A_new100 = recoverBySVD(A, 100)
    A_new120 = recoverBySVD(A, 120)
    A_new150 = recoverBySVD(A, 150)
    plotImg2(*(('30',A_new30),('50',A_new50),('100',A_new100),('120',A_new120),('150',A_new150)))

    

