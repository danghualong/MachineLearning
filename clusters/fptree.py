import numpy as np

class TreeNode(object):
    def __init__(self,name,count):
        self.name=name
        self.count=count
        self.sibling=None
        self.parent=None
        self.children=[]

    def addChild(self,childNode):
        self.children.append(childNode)
    
class FPTree(object):
    def __init__(self,minSup):
        self._minSup=minSup
    
    def createTree(self,frozenItems):
        self.head=TreeNode('HEAD',0)
        self.headerTable={}
        for item in frozenItems:
            for k in item:
                self.headerTable[k]=self.headerTable.get(k,0)+frozenItems[item]
        keys=self.headerTable.keys()
        for key in list(keys):
            if(self.headerTable[key]<self._minSup):
                del(self.headerTable[key])
        for key in self.headerTable:
            self.headerTable[key]=[self.headerTable[key],None]
        # 每个条件模式基和数量
        for item,count in frozenItems.items():
            # 条件模式基中，每个元素的数量，便于后续按照大小排序元素
            localData={}
            for k in item:
                if(k in self.headerTable.keys()):
                    localData[k]=self.headerTable[k][0]
            # 按照headerTable中出现频率排序item(为了处理频率相同者，按键值排序,此处是kv[1]和kv[0],而不是kv[1])
            tmpItem=sorted(localData.items(),key=lambda kv:(kv[1],kv[0]),reverse=True)
            orderedItem=[k[0] for k in tmpItem]
            # print(orderedItem)
            # 将节点添加到树中
            self._addItemToTree(orderedItem,count)
    
    def _addItemToTree(self,orderedItem,count):
        curNode=self.head
        for k in orderedItem:
            isFound=False
            for node in curNode.children:
                if(k==node.name):
                    node.count+=count
                    curNode=node
                    isFound=True
            if(not isFound):
                node=TreeNode(k,count)
                curNode.children.append(node)
                node.parent=curNode
                curNode=node
                headerLink=self.headerTable[k][1]
                if(headerLink==None):
                    self.headerTable[k][1]=curNode
                else:
                    self._updateHeader(self.headerTable[k][1],curNode)
                # print(headerLink)

    def _updateHeader(self,headerLink,curNode):
        while(headerLink.sibling!=None):
            headerLink=headerLink.sibling
        headerLink.sibling=curNode         

    def getPrefix(self):
        condParts={}
        for key in self.headerTable:
            subParts=self.getSinglePrefix(key)
            for tmpKey in subParts:
                if(tmpKey not in condParts):
                    condParts[tmpKey]=subParts[tmpKey]
                else:
                    condParts[tmpKey]+=subParts[tmpKey]
        return condParts 
    
    def getSinglePrefix(self,key):
        node=self.headerTable[key][1]
        condParts={}
        while(node!=None):
            prefixes=[]
            parentNode=node.parent
            while(parentNode!=None and parentNode.count!=0):
                prefixes.append(parentNode.name)
                parentNode=parentNode.parent
            if(len(prefixes)>0):
                frozenPrefixes=frozenset(prefixes)
                if(frozenPrefixes not in condParts):
                    condParts[frozenPrefixes]=0
                condParts[frozenPrefixes]+=node.count
            node=node.sibling
        return condParts

    def displayHeaderTable(self,k):
        curNode=self.headerTable[k][1]
        while(curNode!=None):
            print('node count:',curNode.count)
            curNode=curNode.sibling

    def display(self):
        self._displayTree(self.head,0)
                
    def _displayTree(self,node,ind=0):
        if(node!=None):
            print('{0}{1}--{2}'.format('  '*ind,node.name,node.count))
        if(node.children!=None):
            for subNode in node.children:
                self._displayTree(subNode,ind+1)


def getFrozenItems(items):
    frozenItems={}
    for item in items:
        frozenItem=frozenset(item)
        # frozenItems[frozenItem]=1
        if(frozenItem not in frozenItems):
            frozenItems[frozenItem]=1
        else:
            frozenItems[frozenItem]+=1
    return frozenItems

def minTree(fpTree,minSup,fpset,freqList):
    items=sorted(fpTree.headerTable.items(),key=lambda kv: kv[1][0])
    bigL=[kv[0] for kv in items]
    # print(bigL)
    for basepart in bigL:
        fpsetCopy=fpset.copy()
        fpsetCopy.add(basepart)
        freqList.append(fpsetCopy)
        condParts=fpTree.getSinglePrefix(basepart)
        # print(condParts)
        # print("fpsetcopy:",fpsetCopy)
        tree=FPTree(minSup)
        tree.createTree(condParts)
        # print("tree headerTable")
        # print(tree.headerTable)
        # tree.display()
        if(tree.headerTable!=None and len(tree.headerTable)>0):
            minTree(tree,minSup,fpsetCopy,freqList)
            
    



if __name__=='__main__':
    minSup=3
    fpTree=FPTree(minSup)
    items=[
        ['r','z','h','j','p'],
        ['z','y','x','w','v','u','t','s'],
        ['z'],
        ['r','x','n','o','s'],
        ['y','r','x','z','q','t','p'],
        ['y','z','x','e','q','s','t','m']
    ]
    frozenItems=getFrozenItems(items)
    fpTree.createTree(frozenItems)
    fpTree.display()
    # condParts=fpTree.getPrefix()
    # print(condParts)
    freqList=[]
    minTree(fpTree,minSup,set([]),freqList)
    print("freqList:")
    print(freqList)



