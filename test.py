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

import tensorflow as tf

arr=np.eye(4)
indices=np.arange(4)
np.random.shuffle(indices)
brr=arr[indices]
print(brr)

