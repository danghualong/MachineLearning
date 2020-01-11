import random 


def sort(arr):
    mergeSort(arr,0,len(arr)-1)

def mergeSort(arr,startIndex,endIndex):
    if(startIndex<endIndex):
        mid=int((startIndex+endIndex)/2)
        mergeSort(arr,startIndex,mid)
        mergeSort(arr,mid+1,endIndex)
        merge(arr,startIndex,endIndex)

def merge(arr,startIndex,endIndex):
    mid=int((startIndex+endIndex)/2)
    left=startIndex
    right=mid+1
    tmpArr=[]
    while(left<=mid and right<=endIndex):
        if(arr[left]>arr[right]):
            tmpArr.append(arr[right])
            right+=1
        else:
            tmpArr.append(arr[left])
            left+=1
    while(left<=mid):
        tmpArr.append(arr[left])
        left+=1
    while(right<=endIndex):
        tmpArr.append(arr[right])
        right+=1
    for i in range(len(tmpArr)):
        arr[i+startIndex]=tmpArr[i]


arr=[4,9,8,7,0,5,2,4]
sort(arr)
print(arr)
        
