
import math


def det(arr):
    if(arr is None or len(arr)<=0 or len(arr[0])<=0):
        return 0
    if(len(arr)!=len(arr[0])):
        return 0
    sum=0
    if(len(arr)==1):
        return arr[0][0]
    elif(len(arr)==2):
        return arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0]
    for rowIndex,row in enumerate(arr):
        sum+=math.pow(-1,rowIndex)*arr[rowIndex][0]*det(minor(arr,rowIndex,0))
    return sum

def minor(arr,i,j):
    result=[]
    for rowIndex in range(len(arr)):
        if(rowIndex==i):
            continue
        tmp=[]
        result.append(tmp)
        for colIndex in range(len(arr[rowIndex])):
            if(colIndex==j):
                continue
            tmp.append(arr[rowIndex][colIndex])
    return result

arr=[[1,2,1],[3,2,5],[4,0,4]]
print(arr)
print(det(arr))

arr2=[[1,1],[2,3]]
print(arr2)
print(det(arr2))

arr3=[[4]]
print(arr3)
print(det(arr3))


        
    