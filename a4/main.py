# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import sympy as sym

def f1(x,y):
    return 2*x**2 - x*y -5*x +1

def f2(x,y):
    return x + 3*math.log(x)-y**2

def diff1x(x0,y0):
    x,y = sym.symbols('x y')
    f = sym.diff(2*x**2 - x*y -5*x +1,x)
    return (f.subs(x,x0)).subs(y,y0)

def diff1y(x0,y0):
    x, y = sym.symbols('x y')
    f = sym.diff(2*x**2 - x*y -5*x +1, y)
    return (f.subs(x, x0)).subs(y, y0)


def diff2x(x0,y0):
    x, y = sym.symbols('x y')
    f = sym.diff(x + 3*sym.log(x)-y**2, x)
    return (f.subs(x, x0)).subs(y, y0)


def diff2y(x0,y0):
    x, y = sym.symbols('x y')
    f = sym.diff(x + 3*sym.log(x)-y**2, y)
    return (f.subs(x, x0)).subs(y, y0)


def g1(x,y):
    return math.sqrt((x*y+5*x-1)/2)

def g2(x,y):
    return math.sqrt(x+3*math.log(x))

def nonlinearsystemNewtonMethod(f1,f2,x0,y0,e):
    xn = x0
    yn = y0
    xn1 = x0 + 1
    yn1 = yn + 1
    count = 0

    while(not(abs(xn1-xn)<e and abs(yn1-yn)<e)):
        count += 1
        xn = xn1
        yn = yn1
        xn1 = xn - (((f1(xn, yn) * diff2y(xn, yn)) - f2(xn, yn) * (diff1y(xn, yn))) / (
                diff1x(xn,yn) * diff2y(xn,yn) - diff2x(xn,yn)* diff1y(xn,yn)))
        yn1 = yn - ((f2(xn, yn) * (diff1x(xn, yn)) - f1(xn, yn) * (diff2x(xn, yn)))/ (
                diff1x(xn, yn) * diff2y(xn, yn) - diff2x(xn, yn) * diff1y(xn, yn)))
    print(xn1)
    print(yn1)
    print(count)
    return

def nonlinearsystemPicardPeano(g1,g2,x0,y0,e):
    xn = x0
    yn = y0
    xn1 = x0 + 1
    yn1 = yn + 1
    count = 0

    while (not (abs(xn1 - xn) < e and abs(yn1 - yn) < e)):
        count += 1
        xn = xn1
        yn = yn1
        xn1 = g1(xn,yn)
        yn1 = g2(xn,yn)

    print(xn1)
    print(yn1)
    print(count)

def nonlinearsystemGaussSeidel(g1,g2,x0,y0,e):
    xn = x0
    yn = y0
    xn1 = x0 + 1
    yn1 = yn + 1
    count = 0

    while (not (abs(xn1 - xn) < e and abs(yn1 - yn) < e)):
        count += 1
        xn = xn1
        yn = yn1
        xn1 = g1(xn, yn)
        yn1 = g2(xn1, yn)

    print(xn1)
    print(yn1)
    print(count)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print(diff2y(4,4))
    nonlinearsystemNewtonMethod(f1,f2,4,4,10**(-6))
    nonlinearsystemPicardPeano(g1,g2,4,4,10**(-6))
    nonlinearsystemGaussSeidel(g1,g2,4,4,10**(-6))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
