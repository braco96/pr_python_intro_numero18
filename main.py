# -*- coding: utf-8 -*-
import re
class Pila:
    def __init__(self): self._d=[]
    def push(self,x): self._d.append(x)
    def pop(self): return self._d.pop() if self._d else None
    def __len__(self): return len(self._d)

class Cola:
    def __init__(self): self._d=[]
    def encolar(self,x): self._d.append(x)
    def desencolar(self): return self._d.pop(0) if self._d else None
    def __len__(self): return len(self._d)

