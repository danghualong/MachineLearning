# encoding=utf-8
from pythonds.trees.binaryTree import BinaryTree as Tree
from pythonds.basic.stack import Stack
from expInterpreter import *

#抽象语法树构建者
class AstBuilder(object):
    @staticmethod
    def buildTree(strExp):
        return ""

#抽象语法树解析器,解析成各种解释器的组合
class ExpressionFactory(object):
    @staticmethod
    def getExp(treeNode):
        if treeNode:
            if treeNode.getRightChild():
                leftNode=treeNode.getLeftChild()
                rightNode=treeNode.getRightChild()
                return   BinaryExpression(treeNode.key,ExpressionFactory.getExp(leftNode),ExpressionFactory.getExp(rightNode))
            elif treeNode.getLeftChild():
                leftNode=treeNode.getLeftChild()
                return UnaryExpression(treeNode.key,ExpressionFactory.getExp(leftNode))
            else:
                return ConstExpression(treeNode.key)


if __name__=="__main__":
    #strExp="-12*(3+5)+6"
    rootNode=Tree("+")
    rootNode.insertRight(6)
    rootNode.insertLeft("*")
    treeNode=rootNode.getLeftChild()
    treeNode.insertLeft("-")
    tmpNode=treeNode.getLeftChild()
    tmpNode.insertLeft(12)
    treeNode.insertRight("+")
    tmpNode=treeNode.getRightChild()
    tmpNode.insertLeft(3)
    tmpNode.insertRight(5)

    exp=ExpressionFactory.getExp(rootNode)
    print exp.interpret()


    
    

    

