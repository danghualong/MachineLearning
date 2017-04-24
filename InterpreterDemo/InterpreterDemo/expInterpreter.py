# encoding=utf-8

class ExpressionBase(object):
    """description of class"""

    def __init__(self):
        if type(self) is ExpressionBase:
            raise TypeError("Can't instantiate from abstract class")

    def setLeftExp(self,leftExp=None):
        self.__leftExp=leftExp
    def setLeftExp(self,rightExp=None):
        self.__rightExp=rightExp

    def getKey(self):
        return self.__key
    def setKey(self,key):
        self.__key=key

    def interpret(self):
        print("interpret method from ExpressionBase")

class ConstExpression(ExpressionBase):
    def __init__(self,num):
        self.__key=num
    def interpret(self):
        return self.__key

class UnaryExpression(ExpressionBase):
    def __init__(self,op,leftExp):
        self.__key=op
        self.__leftExp=leftExp
    def interpret(self):
        if self.__key=="-":
            return -self.__leftExp.interpret()
        else:
            raise TypeError("the operator is not minus character")

class BinaryExpression(ExpressionBase):
    def __init__(self,op,leftExp,rightExp):
        self.__key=op
        self.__leftExp=leftExp
        self.__rightExp=rightExp
    def interpret(self):
        if self.__key=="+":
            return self.__leftExp.interpret()+self.__rightExp.interpret()
        elif self.__key=="-":
            return self.__leftExp.interpret()-self.__rightExp.interpret()
        elif self.__key=="*":
            return self.__leftExp.interpret()*self.__rightExp.interpret()
        elif self.__key=="/":
            if self.__rightExp.interpret()==0:
                raise ZeroDivisionError()
            return self.__leftExp.interpret()/self.__rightExp.interpret()
        else:
            raise TypeError("the operator is not right character")

if __name__=="__main__":
    exp1=UnaryExpression("-",ConstExpression(12))
    exp2=BinaryExpression("+",ConstExpression(3),ConstExpression(5))
    exp3=ConstExpression(6)
    exp12=BinaryExpression("*",exp1,exp2)
    exp=BinaryExpression("+",exp12,exp3)
    print exp.interpret()



