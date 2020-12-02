# This is a sample Python script.
import math
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def f(x):
    return (2*math.pow(x,2) + 1) - 5 *math.cos(10*x)

def find_local_minima(x1,x2):
    golden_ratio = (math.sqrt(5) - 1) / 2
    while(abs(x1-x2) > 0.0001):
        x3 = x1 + (math.pow(golden_ratio,2))* (x2-x1)
        x4 = x1 + (golden_ratio) * (x2 -x1)
        if(f(x3) < f(x4)):
            x1 = x1
            x2 = x4
        else:
            x1 = x3
            x2 = x2
    return x1

def find_local_maxima(x1,x2):
    golden_ratio = (math.sqrt(5) - 1) / 2
    while(abs(x1-x2) > 0.0001):
        x3 = x1 + (golden_ratio**2)* (x2-x1)
        x4 = x1 + (golden_ratio) * (x2 -x1)
        if(f(x3) > f(x4)):
            x1 = x1
            x2 = x4
        else:
            x1 = x3
            x2 = x2
    return x1
# Press the green button in the gutter to run the script.
def delta_x(x,y):
    return 4*x-2*y

def delta_y(x,y):
    return 2*y-2*x-6

def g(x,y):
    return y**2 - 2*x*y - 6*y + 2*x**2+12

def find_local_minima_multivariable(xn,yn,gradient,h):
    xn1 = xn + 1
    yn1 = yn + 1
    while(abs(xn1-xn) > 0.01):
        xn = xn1
        yn = yn1
        xn1 = xn - h*gradient[0](xn,yn)
        yn1 = yn - h*gradient[1](xn,yn)
        if(g(xn1,yn1)<g(xn,yn)):
            h = h*2
        else:
            h = h/2
    return (xn1,yn1)

if __name__ == '__main__':
    print(find_local_minima(-1,0))
    print(find_local_maxima(-1,0))
    x,y = find_local_minima_multivariable(1,1,[delta_x,delta_y],1)
    print(x,y,g(x,y))
    # by maxima, gradient = [4*x-2*y,2*y-2*x-6] for the function y**2 - 2*x*y - 6*y + 2*x**2+12

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
