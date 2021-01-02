# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

#1
'''
def f(x):
    return math.sin(x) + x**5 - 0.2*x + 1


def bissection_iteration(a,b,n):
    c = 0
    for _ in range(n):
        c = (a+b)/2
        if(f(c)*f(a) < 0):
            b = c
        else:
            a = c
    print(c)
    errabs = max(abs(a-c),abs(b-c)) 
    print(errabs)
    print(errabs/c)
            
bissection_iteration(-1,0,6)
'''

#2
'''
def f1(x,y):
    return x**2 - y -1.2

def df1x(x,y):
    return 2*x

def df1y(x,y):
    return -1

def f2(x,y):
    return -x + y**2  - 1

def df2x(x,y):
    return -1

def df2y(x,y):
    return 2*y

def jacobian(x,y):
    return 4*x*y - 1

def newton_iteration_system(x,y,n):
    for _ in range(n):
        hx = -(f1(x,y)*df2y(x,y)-f2(x,y)*df1y(x,y))/jacobian(x,y)
        hy = -(df1x(x,y)*f2(x,y)-df2x(x,y)*f1(x,y))/jacobian(x,y)
        x = x + hx
        y = y + hy
        print(x,y)
        
newton_iteration_system(1,1,2)
'''

#3
'''
def f(x):
    return math.exp(1.5*x)

def df(x):
    return 1.5*math.exp(1.5*x)

def g(x):
    return math.sqrt(1+df(x)**2)

def trapezoid(a,b,h):
    n = int((b-a)/h)
    l = 0
    for i in range(n+1):
        if(i == 0 or i == n): l += g(a)
        else: l += 2*g(a)
        a+=h
    l = l*(h/2)
    return l

def simpson(a,b,h):
    n = int((b-a)/h)
    l = 0
    for i in range(n+1):
        if(i == 0 or i == n): l += g(a)
        elif(i%2 == 1): l += 4*g(a)
        else: l += 2*g(a)
        a+=h
    l = l*(h/3)
    return l

h=0.25
hl = h/2
hll = h/4
l = trapezoid(0,2,h)
ls = simpson(0,2,h)
ll = trapezoid(0, 2, hl)
lls = simpson(0,2,hl)
lll = trapezoid(0,2,hll)
llls = simpson(0,2,hll)
qc = (ll-l)/(lll-ll)
e = (lll-ll)/3
qcs = (lls - ls)/(llls - lls)
es = (llls - lls)
print(h,hl,hll,l,ll,lll,qc,e)
print(h,hl, hll, ls, lls, llls, qcs, es )

'''
#4
'''
def dt(T):
    return -0.25*(T-59)

def euler(t,T,h,n):
    for _ in range(n):
        T += dt(T)*h
        t += h
        print(T,t)

euler(2,2,0.5,2)
'''

#5
'''
B = (math.sqrt(5)-1)/2
A = B**2

def f(x):
    return -5*math.cos(x) + math.sin(x) + 10

def aurea_method(x1,x2,n):
    for _ in range(n):
        x3 = A*(x2-x1) + x1
        x4 = B*(x2-x1) + x1
        print(x1,x2,x3,x4,f(x1),f(x2),f(x3),f(x4))
        if(f(x3) > f(x4)):
            x2 = x4
        else:
            x1 = x3
    return abs(x1-x2)

print(aurea_method(2,4,3))
'''
#6
'''
def z(x,y):
    return 3*x**2 - x*y + 11*y + y**2 - 8*x

def dzx(x,y):
    return 6*x - y - 8

def dzy(x,y):
    return -x + 11 +2*y

def gradient(x,y,h, n):
    for _ in range(n):
        print(x,y, z(x,y), dzx(x,y), dzy(x,y))
        newx = x - h*dzx(x,y)
        newy = y - h*dzy(x,y)
        if(z(newx,newy) < z(x,y)):
            h *= 2
            x = newx
            y = newy
        else:
            h /= 2
            
gradient(2,2,1,2)
gradient(2,2, 0.5, 2)
gradient(2,2,0.25,2)
'''