import numpy as np
from abc import ABCMeta,abstractmethod


class Context(metaclass=ABCMeta):
    def __init__(self):
        self._state=CloseState(self)

    def setState(self,state):
        self._state=state
    
    def getState(self):
        return self._state
    
    def open(self):
        self._state.open()

    def close(self):
        self._state.close()

class State(metaclass=ABCMeta):
    def __init__(self,context):
        self._context=context
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def close(self):
        pass

def singleton(cls):
    def _singleton(cls,*args,**kwargs):
        if not hasattr(cls, "_instance"):
            print("hhe")
            cls._instance = cls(*args, **kwargs)
        return cls._instance
    return _singleton


class OpenState(State):
    def open(self):
        print("have already open")
    def close(self):
        self._context.setState(CloseState(self._context))
        print('changed State')

class CloseState(State):
    def open(self):
        self._context.setState(OpenState(self._context))
        print('changed State')
    def close(self):
        print("have already closed")


# mvo=Context()
# print(mvo.getState())
# mvo.close()
# mvo.open()
# print(mvo.getState())
# mvo.close()
# print(mvo.getState())

# import tensorflow as tf
# x=tf.constant(10.0)
# with tf.GradientTape() as tape:
#     tape.watch(x)
#     y=x*x
# grads=tape.gradient(y,x)

# print(grads.numpy())

a=[1,2,3]
b=[1,3]
c=[3,4]
d=[2,3]

def issubset(sub,scope):
    for item in sub:
        if(item not in scope):
            return False
    return True
# b=frozenset(b)
# c=frozenset(c)
# d=frozenset(d)
print(c==d)
print(issubset(b,a))
print(issubset(c,a)) 

d=np.array([3,4,5,7,2,1])
y=np.argsort(d)
y=y[-1:-3:-1]
print(y)