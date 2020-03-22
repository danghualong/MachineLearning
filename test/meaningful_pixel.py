import numpy as np
from PIL import Image,ImageDraw,ImageFont
import cv2

def edit_img(path):
    img=cv2.imread(path)
    print(img.shape)
    
    # cv2.imshow('img',img)
    # cv2.waitKey(0)
    imgrgb=img[:,:,(2,1,0)]
    h=img.shape[0]
    w=img.shape[1]

    canvas=Image.new("RGB",[w,h],'white')
    painter=ImageDraw.Draw(canvas)
    text='党语萱党秉宸'
    textLen=len(text)
    size=10
    font=ImageFont.truetype('C:/Windows/Fonts/Microsoft YaHei UI/msyhbd.ttc',size=size-1)
    for i in range(0,h,size):
        for j in range(0,w,size):
            hend=h if h<i+size else i+size
            wend=w if w<j+size else j+size
            r=np.mean(img[i:hend,j:wend,0]).astype(int)
            g=np.mean(img[i:hend,j:wend,1]).astype(int)
            b=np.mean(img[i:hend,j:wend,2]).astype(int)
            painter.ink=r*256*256+g*256+b
            painter.text((j,i),text[int(j/size)%textLen],font=font)
    canvas.save('./test/imgs/result.jpg','jpeg')

    timg=cv2.imread('./test/imgs/result.jpg')
    cv2.namedWindow('timg', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('timg',timg)
    cv2.waitKey(0)


edit_img('./test/imgs/a.jpg')

