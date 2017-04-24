
def welcome(name):
    return "Hello "+name

class Classifier(object):

    def __init__(self):
        #do nothing
        self.__names=[]
    def addName(self,name):
        self.__names.append(name)
    def getCount(self):
        return len(self.__names)

    def getName(self,index):
        return self.__names[index]

    def classify(self):
        short=[]
        long=[]
        for name in self.__names:
            if len(name)>5:
                long.append(name)
            else:
                short.append(name)
        return short,long
