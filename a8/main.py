# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def f1(x,y,z):
#    return z*y + x

def f1(x,y,z):
    return z

#def f2(x,y,z):
#    return z*x + y

def f2(x,y,z):
    return x -3*z -2*y

def euler(x,y,z,xf,n):
    h = (xf-x)/n
    for _ in range(n):
        x1 = x + h
        y1 = y+h*f1(x,y,z)
        z1 = z+h*f2(x,y,z)
        x = x1
        y = y1
        z = z1
    return (y,z)

def runge_kutta_2(x,y,z,xf,n):
    h = (xf-x)/n
    for _ in range(n):
        x1 = x + h
        y1 = y + h * f1(x + h / 2, y + (h / 2) * f1(x,y,z), z + (h / 2) *f2(x,y,z))
        z1 = y + h * f2(x + h / 2, y + (h / 2) * f1(x,y,z), z + (h / 2) *f2(x,y,z))
        x = x1
        y = y1
        z = z1
    return (y,z)

def runge_kutta_4(x,y,z,xf,n):
    h = (xf-x)/n
    for _ in range(n):
        dy1 = h*f1(x,y,z)
        dz1 = h*f2(x,y,z)
        dy2 = h*f1(x+h/2,y+dy1/2,z+dz1/2)
        dz2 = h*f2(x+h/2,y+dy1/2,z+dz1/2)
        dy3 = h*f1(x+h/2,y+dy2/2,z+dz2/2)
        dz3 = h*f2(x+h/2,y+dy2/2,z+dz2/2)
        dy4 = h*f1(x+h,y+dy3,z+dz3)
        dz4 = h*f2(x+h,y+dy3,z+dz3)
        x1 = x + h
        y1 = y + (1/6)*dy1 + (1/3)*dy2 + (1/3)*dy3 + (1/6)*dy4
        z1 = z + (1/6)*dz1 + (1/3)*dz2 + (1/3)*dz3 + (1/6)*dz4
        x = x1
        y = y1
        z = z1
    return (y,z)
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    n = 20
    s = runge_kutta_4(0,0,0,0.5,n)
    sl = runge_kutta_4(0,0,0,0.5,2*n)
    sll = runge_kutta_4(0,0,0,0.5,4*n)
    qcy = (sl[0]-s[0])/(sll[0]-sl[0])
    qcz = (sl[1] - s[1]) / (sll[1] - sl[1])
    print(s,qcy)
    print(sl,qcz)
    print(sll)
    error1 = (sll[0]-sl[0])/15
    error2 = (sll[1]-sl[1])/15
    print(error1,error2)
    #print(runge_kutta_2(0, 1, 1, 0.5, n))
    #print(runge_kutta_4(0, 1, 1, 0.5, n))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
