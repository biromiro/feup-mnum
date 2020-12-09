# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

def f1(x,y):
    return (x+1)**2 + (y-4)**2

def nabla(x,y):
    return (2*(x+1),2*(y-4))

def inverseH(x,y):
    return (0.5,0,0,0.5)
def quadratic_method(xn,yn,f):

    xn1 = 0.5
    yn1 = 0.5

    while(abs(xn1-xn) > 10**(-6) or abs(yn1-yn) > 10**(-6)):
        xn = xn1
        yn = yn1
        inverseh = inverseH(xn,yn)
        nablaf = nabla(xn,yn)
        xn1 = xn - (inverseh[0]*nablaf[0] + inverseh[1]*nablaf[1])
        yn1 = yn - (inverseh[2]*nablaf[0] + inverseh[3]*nablaf[1])
    return (xn1,yn1)

def evenbergmarquardt_method(xn,yn,lambd):
    xn1 = 0.5
    yn1 = 0.5
    toChange = True

    while(abs(xn1-xn) > 10**(-4) or abs(yn1-yn) > 10**(-4)):
        if(toChange):
            xn = xn1
            yn = yn1
        inverseh = inverseH(xn,yn)
        nablaf = nabla(xn,yn)
        fxnyn = f1(xn,yn)
        xn1 = xn - (inverseh[0]*nablaf[0] + inverseh[1]*nablaf[1] + lambd*nablaf[0])
        yn1 = yn - (inverseh[2]*nablaf[0] + inverseh[3]*nablaf[1] + lambd*nablaf[1])
        fxn1yn1 = f1(xn1,yn1)
        if(fxnyn > fxn1yn1):
            lambd /= 2
            toChange = True
        else:
            lambd *= 2
            toChange = False
    return (xn1,yn1)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print(quadratic_method(1,1,f1));
    print(evenbergmarquardt_method(0,0,0.1))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
