#encoding=utf-8
import numpy as  np
import math
import struct
import arrayUtil as au

map={1:'PW1',16:'CW',-32768:'PW2'}
#The length of the scan line
scanLineSizes={}
#The next scan line number 
expectedLineNOs={}
#The total valid bytes for the scanline
validNums={}
#The latest content in the packet
rawData={}
#The header just with 0x7FFF
isPrintFirstNOs={}




def readData(fileName):
    blockSize=512
    with open(fileName,'rb') as f:
        while True:
            data=f.read(blockSize)
            if data:
                yield data
            else:
                return

def saveData(data):
    #get the first element in the tuple??the return value of unpack_from is tuple)
    chNO=struct.unpack_from('<h',data,24)[0]
    if not rawData.has_key(chNO):
        rawData[chNO]=[au.MyArray([]) for i in range(2)]
        validNums[chNO]=[-1,-1]
        expectedLineNOs[chNO]=[0,0]
        isPrintFirstNOs[chNO]=False
        scanLineSizes[chNO]=0
    #The data in I's Part
    for j in range(36,268,4):
        item=struct.unpack_from('<l',data,j)[0]
        rawData[chNO][0].append(item)
    #The data in Q's Part
    for j in range(268,500,4):
        item=struct.unpack_from('<l',data,j)[0]
        rawData[chNO][1].append(item)
    return chNO

def validateData(chNO,partKey):
    nPart=(0 if partKey=="I" else 1)
    myArr=rawData[chNO][nPart]
    totalLen=myArr.count()
    # remove the data which doesn't belong to the scan line header
    if(totalLen>0 and myArr.getItem(0)!=0x7FFF):
        for i in range(totalLen):
            if(myArr.getItem(i)==0x7FFF):
                if(i+1<totalLen):
                    if(myArr.getItem(i+1)==0x00):
                        myArr.move(i)
                        break
    else:
        if(not isPrintFirstNOs[chNO]):
            scanLineSizes[chNO]=myArr.getItem(3)
            curHeadNO=myArr.getItem(2)
            isPrintFirstNOs[chNO]=True
            print ("The first line header no is %s for channel %d" %(hex(curHeadNO),chNO))
        while(scanLineSizes[chNO]<=totalLen):
            curHeadNO=myArr.getItem(2)
            scanLineSizes[chNO]=myArr.getItem(3)
            if(not(myArr.getItem(0)==0x7FFF and myArr.getItem(1)==0x00)):
                print("!!!!Not Line Header at LineNO %s for channel %d" %(hex(curHeadNO),chNO))
                return
            myArr.move(scanLineSizes[chNO])
            totalLen=myArr.count()

            if(expectedLineNOs[chNO][nPart]==0):
                expectedLineNOs[chNO][nPart]=curHeadNO
            else:
                expectHeadNO=(expectedLineNOs[chNO][nPart]+1)%0x10000
                if expectHeadNO==0:
                    expectHeadNO=1
                expectedLineNOs[chNO][nPart]=expectHeadNO
                if(expectHeadNO!=curHeadNO):
                    print("In channel part(%d,%s): expect headNO is %s,actual headNO is %s" %(chNO,partKey,hex(expectHeadNO),hex(curHeadNO)))
                    return

                

if __name__=="__main__":
    for data in readData(r'D:\12.dat'):
        chNO=saveData(data)
        validateData(chNO,"I")
        validateData(chNO,"Q")
        
    print "valid completed"
    #str="a+b*{c*[d+e*(a+b)]}*(c+d)"
    #s=[]
    #brakets={"{":"}","[":"]","(":")"}
    #for i in str:
    #    if i in ("{","[","("):
    #        s.append(i)
    #    elif i in (")","]","}"):
    #        if len(s)<=0:
    #            print "no left braket which matches the right braket %s",i
    #            break
    #        actual=s.pop()
    #        if(brakets[actual]!=i):
    #            expectedKey=(key for key in brakets.keys() if brakets[key]==i).next()
    #            print "expected braket is %s,actual is %s" %(expectedKey,actual)
    #            break
        
