# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:46:54 2021

@author: nrtc
"""
import math

'''
def f(x,y):
    return y**2 - 2*x*y - 6*y + 2*x**2 +12

def dfx(x,y):
    return -2*y + 4*x

def dfy(x,y):
    return 2*y - 2*x - 6

def gradient(x0,y0,e,h):
    it = 0
    new_x = x0 + 1
    new_y = y0 + 1
    first = True
    while(abs(new_x-x0) > e or abs(new_y-y0) > e):
        if(first):
            first = False
        else:
            x0 = new_x
            y0 = new_y
        new_x = x0 - h*dfx(x0,y0)
        new_y = y0 - h*dfy(x0,y0)
        if(f(new_x, new_y) < f(x0,y0)):
            h *= 2
        else:
            h /= 2
        it += 1
        print(it, h, new_x, new_y, f(new_x,new_y), abs(new_x - x0), abs(new_y - y0))
    return (new_x,new_y)
'''
'''
def f(x,y):
    return math.sin(x/2) + x**2 - math.cos(y)

def gradient(x,y):
    return [2*x + math.cos(x/2)/2, math.sin(y)]

def inverse_hessian(x,y):
    return [[1/(2 - math.sin(x/2)/4), 0],[0, 1/math.cos(y)]]


def quadric(x0,y0,e):
    x = x0 + 1
    y = y0 + 1
    first = True
    it = 0
    while(abs(x-x0) > e or abs(y-y0) > e):
        if(first):
            first = False
        else:
            x0 = x
            y0 = y
        h = inverse_hessian(x0,y0)
        gr = gradient(x0,y0)
        x = x0 - (h[0][0]*gr[0] + h[0][1]*gr[1])
        y = y0 - (h[1][0]*gr[0] + h[1][1]*gr[1])
        it += 1
        print(it,x0,y0,h[0][0],h[0][1],h[1][0],h[1][1],x,y,f(x,y), abs(x-x0), abs(y-y0))
    
print(quadric(-3,-1,0.001))
'''
'''
B = (math.sqrt(5)-1)/2
A = B**2

def f(x):
    return (2*x +1)**2 - 5*math.cos(10*x)


def aurea_min(x1,x2,e):
    while(abs(x1-x2) > e):
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        if(f(x3) < f(x4)):
            x2 = x4
        else:
            x1 = x3
    return (x1 + x2)/2

def aurea_max(x1,x2,e):
    while(abs(x1-x2) > e):
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        if(f(x3) > f(x4)):
            x2 = x4
        else:
            x1 = x3
    return (x1 + x2)/2
minimum =  aurea_min(-1,0,0.001)
maximum = aurea_max(-1,0,0.001)
print(minimum, f(minimum))
print(maximum, f(maximum))
'''
def f(x,y):
    return math.sin(x/2) + x**2 - math.cos(y)

def gradient(x,y):
    return [2*x + math.cos(x/2)/2, math.sin(y)]

def inverse_hessian(x,y):
    return [[1/(2 - math.sin(x/2)/4), 0],[0, 1/math.cos(y)]]

def lm(x0,y0,e,h):
    x = x0 + 1
    y = y0 + 1
    first = True
    it = 0
    while(abs(x-x0) > e or abs(y-y0) > e):
        if(first):
            first = False
        else:
            x0 = x
            y0 = y
            
        hessian = inverse_hessian(x0,y0)
        grad = gradient(x0,y0)
        h_x_quad = hessian[0][0]*grad[0] + hessian[0][1]*grad[1]
        h_y_quad = hessian[1][0]*grad[0] + hessian[1][1]*grad[1]
        h_x_grad = h*grad[0]
        h_y_grad = h*grad[1]
        h_x = h_x_quad + h_x_grad
        h_y = h_y_quad + h_y_grad
        x = x0 - h_x
        y = y0 - h_y
        if(f(x,y) < f(x0,y0)):
            h *= 2
        else:
            h /= 2
        it += 1
        print(it,x0,y0,hessian[0][0],hessian[0][1],hessian[1][0],hessian[1][1],x,y,f(x,y), abs(x-x0), abs(y-y0))
    return (x,y)

print(lm(-10,-1,0.001,0.01))