# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 20:11:50 2021

@author: exame
"""


def f(x):
    return x**3 + 2*x**2 + 10*x -12

def dfx(x):
    return 3*x**2 + 4*x + 10

def newton_method(x0,n):
    for _ in range(n):
        print(x0)
        x0 = x0 - f(x0)/dfx(x0)
    
    
newton_method(0,3)