#encoding=utf-8
import numpy as  np
import struct

map={1:'PW1',16:'CW',-32768:'PW2'}

def readData(fileName):
    chData={}
    with open(fileName,'rb') as f:
        while True:
            data=f.read()
            arrLen=len(data)
            if arrLen<=0:
                break

            for i in range(0,arrLen,512):
                #get the first element in the tuple??the return value of unpack_from is tuple)
                chNO=struct.unpack_from('<h',data,i+24)[0]
                if not chData.has_key(chNO):
                    chData[chNO]=[[],[]]
                for j in range(i+36,i+268,4):
                    item=struct.unpack_from('<l',data,j)[0]
                    chData[chNO][0].append(item)
                for j in range(i+268,i+500,4):
                    item=struct.unpack_from('<l',data,j)[0]
                    chData[chNO][1].append(item)
    return chData

def invalidData(chNO,partKey,iqData):
    headNO=0
    expectHeadNO=0
    size=0
    startIdx=0
    lineNOs=[]
    for i in range(len(iqData)):
        if iqData[i]==0x7FFF and iqData[i+1]==0:
            startIdx=i
            size=iqData[i+3]
            headNO=iqData[i+2]
            expectHeadNO=headNO
            print ("channel %s %s part's init scanLineNO is %s" %(map[chNO],partKey,hex(headNO)))
            break
    for i in range(startIdx,len(iqData),size):
        if iqData[i]==0x7FFF and iqData[i+1]==0:
            headNO=iqData[i+2]
            lineNOs.append(hex(headNO))
            if expectHeadNO!=headNO:
                print ("expect headNO is %s,actual headNO is %s" %(hex(expectHeadNO),hex(headNO)))
                break
            expectHeadNO+=1
        else:
            print("!!!!Not Line Header after LineNO %s" %(hex(expectHeadNO-1)))
            break
    #print lineNOs


if __name__=="__main__":
    chData=readData(r'D:\allFile.dat')
    print "read data completed..."
    
    keys=chData.keys()
    for i in range(len(keys)):
        invalidData(keys[i],"I",chData[keys[i]][0])
        invalidData(keys[i],"Q",chData[keys[i]][1])
    print "valid completed"
        
