# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

import numpy


angle_approx = [0,0.035,0.07,0.1,0.13,0.17,0.2,0.23,0.26,0.3,0.33,0.36,0.4,0.43,0.46,0.495,0.53]


def f1(x):
    return x*0.30*math.cos(angle_approx[2*x])

def f05(x):
    return x*0.3*math.cos(angle_approx[int(2*x)])

def simpson(a,b,h,f):
    return (h/3)*(f(a) + f(b) + 2*sum([2*f(i) if i%2 == 0 else f(i) for i in numpy.arange(a+h,b,h)]))


sll = 2*math.pi*simpson(0,8,0.5,f05)
sl = 2*math.pi*simpson(0,8,1,f1)
s = 2*math.pi*simpson(0,8,2,f1)

print(s,sl,sll)

qc = (sl-s)/(sll-sl)
err = (sll-sl)/16 #unacceptable qc
print(qc,err)

sll = 2*math.pi*simpson(0,8,1,f1)
sl = 2*math.pi*simpson(0,8,2,f1)
s = 2*math.pi*simpson(0,8,4,f1)

print(s,sl,sll)

qc = (sl-s)/(sll-sl)
err = (sll-sl)/16 #unacceptable qc
print(qc,err)
