import numpy as np

def loadData(fileName):
    try:
        lines=None
        with open(fileName) as f:
            lines=f.readlines()
        rows=len(lines)
        if rows<=0:
            return
        cols=len(lines[0].strip().split("\t"))
        mat=[]
        labels=[]
        index=0
        for line in lines:
            line=line.strip()
            items=line.split("\t")
            mat.append([float(item) for item in items[0:-1]])
            labels.append(items[-1])
            index+=1
        return mat,labels
    except Exception as ex:
        print ex


