#encoding=utf-8
import numpy as  np
import math
import struct

map={1:'PW1',16:'CW',-32768:'PW2'}
#The length of the scan line
scanLineSizes={}
#The next scan line number 
expectedLineNOs={}
#The total valid bytes for the scanline
validNums={}
#The latest content in the packet
chData={} 


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
    if not chData.has_key(chNO):
        chData[chNO]=[[],[]]
        validNums[chNO]=[-1,-1]
        expectedLineNOs[chNO]=[0,0]
    #The data in I's Part
    chData[chNO][0]=[]
    chData[chNO][1]=[]
    for j in range(36,268,4):
        item=struct.unpack_from('<l',data,j)[0]
        chData[chNO][0].append(item)
    #The data in Q's Part
    for j in range(268,500,4):
        item=struct.unpack_from('<l',data,j)[0]
        chData[chNO][1].append(item)
    return chNO

def validateData(chNO,partKey):
    nPart=(0 if partKey=="I" else 1)
    iqData=chData[chNO][nPart]
    if(validNums[chNO][nPart]==-1):
        for i in range(len(iqData)):
            if iqData[i]==0x7FFF and iqData[i+1]==0:
                expectedLineNOs[chNO][nPart]=iqData[i+2]
                scanLineSizes[chNO]=iqData[i+3]
                if(scanLineSizes[chNO]<=0):
                    break
                validNums[chNO][nPart]=len(iqData)-i
                break
    else:
       validNums[chNO][nPart]+=len(iqData)
       if(validNums[chNO][nPart]>scanLineSizes[chNO]):
           startIdx=len(iqData)+scanLineSizes[chNO]-validNums[chNO][nPart]
           if iqData[startIdx]==0x7FFF and iqData[startIdx+1]==0:
               if(startIdx==56):
                   expectHeadNO=(expectedLineNOs[chNO][nPart]+1)%0x10000
                   if expectHeadNO==0:
                       expectHeadNO=1
                   expectedLineNOs[chNO][nPart]=expectHeadNO
                   validNums[chNO][nPart]-=scanLineSizes[chNO]
                   return

               headNO=iqData[startIdx+2]
               expectHeadNO=(expectedLineNOs[chNO][nPart]+1)%0x10000
               if expectHeadNO==0:
                   expectHeadNO+=1
               if expectHeadNO!=headNO:
                   print("In channel part(%d,%s): expect headNO is %s,actual headNO is %s" %(chNO,partKey,hex(expectHeadNO),hex(headNO)))
                   return
               else:
                   expectedLineNOs[chNO][nPart]=expectHeadNO
                   validNums[chNO][nPart]-=scanLineSizes[chNO]
           else:
                print("!!!!Not Line Header after LineNO %s for channel %d" %(hex(expectedLineNOs[chNO][nPart]),chNO))
                return


if __name__=="__main__":
    for data in readData(r'D:\1.dat'):
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
        
