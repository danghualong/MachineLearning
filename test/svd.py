import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
# from sklearn import datasets
from skimage import io
import os
dirName=dirName=os.path.dirname(__file__)


# def getImgAsMat(index):
#     ds = datasets.fetch_olivetti_faces()
#     return np.mat(ds.images[index])

def getImgAsMatFromFile(filename):
    img = io.imread(filename,as_gray=True)
    return np.mat(img) 

def plotImg(imgMat):
    plt.imshow(imgMat, cmap=plt.cm.gray)
    plt.show()

def recoverBySVD(imgMat, k):
    # singular value decomposition
    U, s, V = la.svd(imgMat)
    # choose top k important singular values (or eigens)
    Uk = U[:, 0:k]
    #SK:二维数组
    Sk = np.diag(s[0:k])
    Vk = V[0:k, :]
    # recover the image
    imgMat_new = Uk * Sk * Vk
    return imgMat_new


# -------------------- main --------------------- #
#A = getImgAsMat(0)
#plotImg(A)
#A_new = recoverBySVD(A, 20)
#plotImg(A_new)
if __name__=="__main__":
    A = getImgAsMatFromFile('./test/data/niu.jpg')
    plotImg(A)
    A_new = recoverBySVD(A, 50)
    plotImg(A_new)

