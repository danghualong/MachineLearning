#encoding=utf-8

class Factorial(object):
    def multiply(self,n):
        if(n<=0):
            return 1
        if(n>=9):
            raise Exception("The number should not be larger than 8")
        return n*self.multiply(n-1)
