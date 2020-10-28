# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def function1(x):
    return x - 2*math.log(x)-5

def function2(x):
    return 2**(math.sqrt(x))-10*x +1

def function3(x):
    return (1/math.tan(x))*math.sin(3*x)-x+1

def function4(x):
    return x*(math.e)**(x**2 -4)

def bissection_method_absolute_stop(a,b,f):
    i = 0
    while(abs(b-a)>0.000001):
        i+=1
        x = (a+b)/2;
        if((f(a)*f(x))<0):
            b = x
        else:
            a = x
    print(i)
    return x

def bissection_method_null_at_root(a,b,f):
    i = 0
    while(abs(f(a) - f(b)) > 0.000001):
        i+=1
        x = (a+b)/2;
        if((f(a)*f(x))<0):
            b = x
        else:
            a = x
    print(i)
    return x

def bissection_method_two_consecutives_stop(a,b,f):
    i = 0
    x1 = 0
    x2 = 1
    while(abs(x1-x2) > 0.000001):
        i+=1
        x2 = x1
        x1 = (a+b)/2;
        if((f(a)*f(x1))<0):
            b = x1
        else:
            a = x1
    print(i)
    return x1

def rope_method_absolute_stop(a,b,f):
    i = 0
    while (abs(b - a) > 0.000001):
        i += 1
        x = (a*f(b) - b*f(a))/(f(b)-f(a));
        if ((f(a) * f(x)) < 0):
            b = x
        else:
            a = x
    print(i)
    return x

def rope_method_null_at_root(a,b,f):
    i = 0
    while (abs(f(a) - f(b)) > 0.000001):
        i += 1
        x = (a*f(b) - b*f(a))/(f(b)-f(a));
        if ((f(a) * f(x)) < 0):
            b = x
        else:
            a = x
    print(i)
    return x

def rope_method_two_consecutives_stop(a,b,f):
    i = 0
    x1 = 0
    x2 = 1
    while (abs(x1-x2) > 0.000001):
        i += 1
        x2 = x1
        x1 = (a * f(b) - b * f(a)) / (f(b) - f(a));
        if ((f(a) * f(x1)) < 0):
            b = x1
        else:
            a = x1
    print(i)
    return x1

if __name__ == '__main__':
    #print(bissection_method_absolute_stop(-0.001,0.001,function3))
    #print(bissection_method_null_at_root(0.01,1,function1))
    print(bissection_method_two_consecutives_stop(-1,2,function4))
    #print(rope_method_absolute_stop(0.01, 1, function1))
    #print(rope_method_null_at_root(0.01, 1, function1))
    print(rope_method_two_consecutives_stop(-1,2,function4))
    #print(bissection_method_absolute_stop(9,10,function1))
    #print(bissection_method_absolute_stop(0,1,function2))
    #print(bissection_method_absolute_stop(98.5,99.5,function2))
    #print(bissection_method_absolute_stop(0.5,1.5,function3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
