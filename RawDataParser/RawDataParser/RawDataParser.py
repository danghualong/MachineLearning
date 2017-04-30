#encoding=utf-8
import numpy as  np
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
        validNums[chNO]=-1
    #The data in I's Part
    for j in range(36,268,4):
        item=struct.unpack_from('<l',data,j)[0]
        chData[chNO][0]=data;
    #The data in Q's Part
    for j in range(268,500,4):
        item=struct.unpack_from('<l',data,j)[0]
        chData[chNO][1]=data
    return chNO

def validateData(chNO,partKey):
    nPart=(0 if partKey=="I" else 1)
    iqData=chData[chNO][nPart]
    if(validNums[chNO]==-1):
        for i in range(len(iqData)):
            if iqData[i]==0x7FFF and iqData[i+1]==0:
                expectedLineNOs[chNO]=iqData[i+2]
                scanLineSizes[chNO]=iqData[i+3]
                validNums[chNO]=len(iqData)-i
                break
    else:
       validNums[chNO]+=len(iqData)
       if(validNums[chNO]>scanLineSizes[chNO]):
           startIdx=len(iqData)+scanLineSizes[chNO]-validNums[chNO]
           if iqData[startIdx]==0x7FFF and iqData[startIdx+1]==0:
               headNO=iqData[startIdx+2]
               expectHeadNO=(expectedLineNOs[chNO]+1)%0xFFFF
               if expectHeadNO!=headNO:
                   print("In channel part(%d,%s): expect headNO is %s,actual headNO is %s" %(chNO,partKey,hex(expectHeadNO),hex(headNO)))
                   return
               else:
                   expectedLineNOs[chNO]=expectHeadNO
                   validNums[chNO]-=scanLineSizes[chNO]
           else:
                print("!!!!Not Line Header after LineNO %d for channel %d" %(hex(expectedLineNOs[chNO]),chNO))
                return


if __name__=="__main__":
    for data in readData(r'D:\allFile.dat'):
        chNO=saveData(data)
        validateData(chNO,"I")
        validateData(chNO,"Q")
    print "valid completed"
        
