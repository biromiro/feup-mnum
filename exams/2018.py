# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 10:18:47 2021

@author: nrtc
"""
import math

#1

'''
def f1(x,y):
    return math.sin(x+y) - math.exp(x-y)

def f2(x,y):
    return math.cos(x+y) - (x**2)*(y**2)

def df1x(x,y):
    return math.cos(x+y) - math.exp(x-y)

def df1y(x,y):
    return math.cos(x+y) + math.exp(x-y)

def df2x(x,y):
    return -math.sin(x+y) -2*x*(y**2)

def df2y(x,y):
    return -math.sin(x+y) -2*(x**2)*y

def jacobian(x,y):
    return (math.cos(x+y)-math.exp(x-y))*((-math.sin(x+y)) - 2*(x**2)*y) - (math.cos(x+y)+ math.exp(x-y))*((-math.sin(x+y))-2*x*(y**2))

def newton_system(x,y,n):
    for _ in range(n):
        h = -(f1(x,y)*df2y(x,y) - f2(x,y)*df1y(x,y))/jacobian(x,y)
        k = -(df1x(x,y)*f2(x,y) - df2x(x,y)*f1(x,y))/jacobian(x,y)
        x += h
        y += k
        print(x,y)

newton_system(0.5,0.25,2)
'''
#2
'''
A = [[103,61,41],[1,5.5,3],[2,10,13]]
B = [[2,10,13],[1,5.5,3],[103,61,41]]
C = [[1,5.5,3],[103,61,41],[2,10,13]]

def meets_convergence(matrix):
    for i,row in enumerate(matrix):
        total = sum(row) - row[i]
        if(total >= row[i]):
            return False
        
    return True

print(meets_convergence(A))
print(meets_convergence(B))
print(meets_convergence(C))

# a) -> Only matrix A meets convergence, so it must be the one that is chosen
# b) -> Matrix B produces exact results on maxima, while the others give approximations
# c) 
# xn+1 = (1.2 -61yn - 41zn)/103 
# yn+1 = (0 -5.5yn -3zn)/1  
# zn+1 = (-13 -10yn -13zn)/2
'''

#3

'''
hx = 1
hy = 1

def f(x,y):
    if(x==0 and y==0): return 1.1
    elif(x==0 and y ==1): return 2.1
    elif(x==0 and y==2): return 7.8
    elif(x==1 and y == 0): return 1.4
    elif(x==1 and y==1): return 4
    elif(x==1 and y==2): return 1.5
    elif(x==2 and y==0): return 9.8
    elif(x==2 and y==1): return 2.2
    elif(x==2 and y==2): return 1.2
def simpson_double_int():
    return (hx*hy/9)*(f(0,0)+f(0,2)+f(2,0)+f(2,2)+
                      4*(f(0,1)+f(1,0)+f(1,2)+f(2,1))+
                      16*f(1,1))

print(simpson_double_int())
'''

#4
'''
# dy/dx = z  e dz/dx = Az - By

A = -7
B = 4

def dyx(x,y,z):
    return z

def dzx(x,y,z):
    return A*z - B*y

def euler(x,y,z,n,h):
    for _ in range(n):
        dy = h*dyx(x,y,z)
        dz = h*dzx(x,y,z)
        x += h
        y += dy
        z += dz
        print(x,y,z)
        
# h = 0.2

euler(0.4,2,1,3,0.2)
'''

#5
#single variable function(x)
#thirds method, golden ratio or any simple search
'''
B = (math.sqrt(5)-1)/2
A = B**2
a = 2

def f(x):
    return (x-a)**2 + x**4

def dfx(x):
    return 2*(x-a) + 4*x**3

def d2fx(x):
    return 2 + 12*x**2

def golden_ratio(x1,x2):
    while(abs(x1-x2) > 0.000001):
        x3 = A*(x1-x2) + x1
        x4 = B*(x1-x2) + x1
        if(f(x3) < f(x4)):
            x2 = x4
        else:
            x1 = x3
    return (x1+x2)/2

def newton_zero(x):
    while(abs(dfx(x)) > 0.000001):
        x = x - dfx(x)/d2fx(x)
    return x

print(golden_ratio(0.5,1))
print(newton_zero(0.5))
'''

#6
'''
a = 0.4523 * 10**4
b = 0.2115 * 10**(-3)
c = 0.2583 * 10**1

a+b+c -> tudo em expoente 4
b = 0.0000 * 10 ** 4
c = 0.0002 * 10 ** 4
a = 0.4523 * 10 ** 4
+_______________
r = 0.4525 * 10 ** 4

a  + b + c = 4523 + 2.583 + 0.0002115 = 4525.5832115

erro absoluto = 4525 - 4525.5832115 = -0.5832 * 10 ** 0
erro relativo = erro absoluto * 100/ (a+b+c real) = 0.1288 * 10 ** -1

'''
























