import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


def test_pila_cola():
    p = mod.Pila(); c = mod.Cola()
    p.push(1); p.push(2); assert len(p)==2; assert p.pop()==2
    assert p.pop()==1; assert p.pop() is None
    c.encolar(5); c.encolar(7); assert len(c)==2
    assert c.desencolar()==5; assert c.desencolar()==7; assert c.desencolar() is None
