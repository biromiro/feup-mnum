import math
import matplotlib.pyplot as plt
import time

dt = 0
vap = 3250
ket =  0.0015983333333333/60
#ke = ket*vap
tmax = 5*60
ka = 0
'''
@brief administration function

@param t time elapsed
'''
def d(t):
    res = 0
    res += 9*10**3*t*pow(math.e,-3*t)
    if(t > 86400): res += 9*10**3*(t-86400)*pow(math.e,-3*(t-86400))
    if(t > 172800): res += 9*10**3*(t-172800)*pow(math.e,-3*(t-172800))
    if(t > 259200): res += 9*10**3*(t-259200)*pow(math.e,-3*(t-259200))
    return res

'''
@brief derivative of the ka-ket equation

@param x0 x position to calculate
'''
def diffg1(x0):
    return pow(math.e,-tmax*x0) - tmax*x0*pow(math.e,-tmax*x0)

'''
@brief ka-ket equation

@param x x position to calculate
'''
def g1(x):
    return x*pow(math.e,-x*tmax)-ket*pow(math.e,-ket*tmax)

'''
@brief ridders zero's method with absolute stop

@param a left interval limit
@param b right interval limit
@param f function to test
'''
def false_position_ridders_absolute(a,b,f):
    count = 0
    ans = 9999
    while(True):
        count += 1
        x = (a + b) / 2
        fx = f(x)
        s = math.sqrt(fx*fx - f(a)*f(b))
        xnew = 0
        if(f(a)>=0):
            xnew = x + (x-a)*(fx/s)
        else:
            xnew = x + (x-a)*(-fx/s)
        ans = xnew
        fnew = f(ans)
        if(abs(a-b) <= 0.000001): break
        if(fx*f(xnew)<0):
            a = x
            b = xnew
        elif(f(a)*f(xnew)<0):
            a = a
            b = xnew
        else:
            a = xnew
            b = b
    print(count)
    return ans

''' 
@brief ridders zero's method with relative stop

@param a left interval limit
@param b right interval limit
@param f function to test
'''
def false_position_ridders_relative(a,b,f):
    count = 0
    ans = 9999
    while(True):
        count += 1
        x = (a + b) / 2
        fx = f(x)
        s = math.sqrt(fx*fx - f(a)*f(b))
        xnew = 0
        if(f(a)>=0):
            xnew = x + (x-a)*(fx/s)
        else:
            xnew = x + (x-a)*(-fx/s)
        ans = xnew
        fnew = f(ans)
        if(abs((a-b)/a) <= 0.000001): break
        if(fx*f(xnew)<0):
            a = x
            b = xnew
        elif(f(a)*f(xnew)<0):
            a = a
            b = xnew
        else:
            a = xnew
            b = b
    print(count)
    return ans

''' 
@brief ridders zero's method with function anullment stop

@param a left interval limit
@param b right interval limit
@param f function to test
'''
def false_position_ridders_function_annulment(a,b,f):
    count = 0
    ans = 9999
    while(True):
        count += 1
        x = (a + b) / 2
        fx = f(x)
        s = math.sqrt(fx*fx - f(a)*f(b))
        xnew = 0
        if(f(a)>=0):
            xnew = x + (x-a)*(fx/s)
        else:
            xnew = x + (x-a)*(-fx/s)
        ans = xnew
        fnew = f(ans)
        if(abs(f(a)-f(b)) <= 0.000001): break
        if(fx*f(xnew)<0):
            a = x
            b = xnew
        elif(f(a)*f(xnew)<0):
            a = a
            b = xnew
        else:
            a = xnew
            b = b
    print(count)
    return ans

''' 
@brief newton zero's method with absolute stop

@param x0 initial guess
@param e max error
'''
def newton_method_absolute(x0,e):
    xn = x0
    xn1 = x0 + 0.01
    count = 0

    while(abs(xn-xn1)>e):
        count += 1
        xn = xn1
        xn1 = xn - (g1(xn) / diffg1(xn))
    print(count)
    return xn1

''' 
@brief newton zero's method with relative stop

@param x0 initial guess
@param e max error
'''
def newton_method_relative(x0,e):
    xn = x0
    xn1 = x0 + 0.01
    count = 0

    while(abs((xn-xn1)/xn)>e):
        count += 1
        xn = xn1
        xn1 = xn - (g1(xn) / diffg1(xn))
    print(count)
    return xn1

''' 
@brief newton zero's method with function anullment stop

@param x0 initial guess
@param e max error
'''
def newton_method_function_annulment(x0,e):
    xn = x0
    xn1 = x0 + 0.01
    count = 0

    while(abs(g1(xn)-g1(xn1))>e):
        count += 1
        xn = xn1
        xn1 = xn - (g1(xn) / diffg1(xn))
    print(count)
    return xn1

''' 
@brief regula falsi zero's method with absolute stop

@param a left interval limit
@param b right interval limit
@param f function to test
'''
def regula_falsi_absolute(a,b,f):
    i = 0
    while (abs(a-b) > 0.000001):
        i += 1
        x = (a*f(b) - b*f(a))/(f(b)-f(a))
        if ((f(a) * f(x)) < 0):
            b = x
        else:
            a = x
    print(i)
    return x

'''
@brief regula falsi zero's method with relative stop

@param a left interval limit
@param b right interval limit
@param f function to test
'''
def regula_falsi_relative(a,b,f):
    i = 0
    while (abs((a-b)/a) > 0.000001):
        i += 1
        x = (a*f(b) - b*f(a))/(f(b)-f(a))
        if ((f(a) * f(x)) < 0):
            b = x
        else:
            a = x
    print(i)
    return x

''' 
@brief regula falsi zero's method with function anullment stop

@param a left interval limit
@param b right interval limit
@param f function to test
'''
def regula_falsi_function_annulment(a,b,f):
    i = 0
    while (abs(f(a)-f(b)) > 0.000001):
        i += 1
        x = (a*f(b) - b*f(a))/(f(b)-f(a))
        if ((f(a) * f(x)) < 0):
            b = x
        else:
            a = x
    print(i)
    return x

''' 
@brief brent zero's method with absolute stop

@param a left interval limit
@param b right interval limit
@param f function to test
'''
def brent_method_absolute(a,b,f):
    count  = 0
    if(f(a)*f(b)>=0): return
    if(abs(f(a)) < abs(f(b))):
        tmp = a
        a = b
        b = tmp
    c = a
    mflag = True
    s = 0
    d = 0
    delta = 0.000001
    while(abs(a-b) > delta):
        count += 1
        if(f(a) != f(c) and f(b) != f(c)):
            s = a*f(b)*f(c)/((f(a)-f(b))*(f(a)-f(c))) + b*f(a)*f(c)/((f(b)-f(a))*(f(b)-f(c))) + c*f(a)*f(b)/((f(c)-f(a))*(f(c)-f(b)))
        else:
            s = b - f(b)*(b-a)/(f(b)-f(a))
        if(not(s>(3*a+b)/4 and s < b) or (mflag and abs(s-b)>= abs(b-c)/2)
        or (not mflag and  abs(s-b) >= abs(c-d)/2) or (mflag and abs(b-c) < abs(delta)) or
                (not mflag and abs(c-d) < abs(delta))):
            s = (a+b)/2
            mflag = True
        else: mflag = False
        d = c
        c = b
        if(f(a)*f(s) < 0):
            b = s
        else:
            a = s
        if (abs(f(a)) < abs(f(b))):
            tmp = a
            a = b
            b = tmp
    print(count)
    return s

''' 
@brief regula falsi zero's method with relative stop

@param a left interval limit
@param b right interval limit
@param f function to test
'''
def brent_method_relative(a,b,f):
    count  = 0
    if(f(a)*f(b)>=0): return
    if(abs(f(a)) < abs(f(b))):
        tmp = a
        a = b
        b = tmp
    c = a
    mflag = True
    s = 0
    d = 0
    delta = 0.000001
    while(abs((a-b)/a) > delta):
        count += 1
        if(f(a) != f(c) and f(b) != f(c)):
            s = a*f(b)*f(c)/((f(a)-f(b))*(f(a)-f(c))) + b*f(a)*f(c)/((f(b)-f(a))*(f(b)-f(c))) + c*f(a)*f(b)/((f(c)-f(a))*(f(c)-f(b)))
        else:
            s = b - f(b)*(b-a)/(f(b)-f(a))
        if(not(s>(3*a+b)/4 and s < b) or (mflag and abs(s-b)>= abs(b-c)/2)
        or (not mflag and  abs(s-b) >= abs(c-d)/2) or (mflag and abs(b-c) < abs(delta)) or
                (not mflag and abs(c-d) < abs(delta))):
            s = (a+b)/2
            mflag = True
        else: mflag = False
        d = c
        c = b
        if(f(a)*f(s) < 0):
            b = s
        else:
            a = s
        if (abs(f(a)) < abs(f(b))):
            tmp = a
            a = b
            b = tmp
    print(count)
    return s

''' 
@brief regula falsi zero's method with function anullment stop

@param a left interval limit
@param b right interval limit
@param f function to test
'''
def brent_method_function_annulment(a,b,f):
    count  = 0
    if(f(a)*f(b)>=0): return
    if(abs(f(a)) < abs(f(b))):
        tmp = a
        a = b
        b = tmp
    c = a
    mflag = True
    s = 0
    d = 0
    delta = 0.000001
    while(abs(f(a)-f(b)) > delta):
        count += 1
        if(f(a) != f(c) and f(b) != f(c)):
            s = a*f(b)*f(c)/((f(a)-f(b))*(f(a)-f(c))) + b*f(a)*f(c)/((f(b)-f(a))*(f(b)-f(c))) + c*f(a)*f(b)/((f(c)-f(a))*(f(c)-f(b)))
        else:
            s = b - f(b)*(b-a)/(f(b)-f(a))
        if(not(s>(3*a+b)/4 and s < b) or (mflag and abs(s-b)>= abs(b-c)/2)
        or (not mflag and  abs(s-b) >= abs(c-d)/2) or (mflag and abs(b-c) < abs(delta)) or
                (not mflag and abs(c-d) < abs(delta))):
            s = (a+b)/2
            mflag = True
        else: mflag = False
        d = c
        c = b
        if(f(a)*f(s) < 0):
            b = s
        else:
            a = s
        if (abs(f(a)) < abs(f(b))):
            tmp = a
            a = b
            b = tmp
    print(count)
    return s

''' 
@brief the first of the two diferential equations

@param t current time
@param mi current mi
@param mp current mp
'''
def f1(t,mi,mp):
    return d(t) - ka*mi

''' 
@brief the second of the two diferential equations

@param t current time
@param mi current mi
@param mp current mp
'''
def f2(t,mi,mp):
    return ka*mi - ket*mp

''' 
@brief euler's system of differential equations solver

@param x x's initial guess
@param y y's initial guess
@param z z's initial guess
@param xf final x to calculate
@param n number of iterations

@return the calculated times and their respective mi, mp, qc of mi, qc of mp, error of mi and error of mp
'''
def euler(x,y,z,xf,n):
    xi = x
    yi = y
    zi = z
    t = []
    mi = []
    mil = []
    mill = []
    mp = []
    mpl = []
    mpll = []
    h = (xf - x) / n
    for i in range(3):
        for j in range(n):
            x1 = x + h
            y1 = y + h*f1(x,y,z)
            z1 = z + h*f2(x,y,z)
            if (i == 0):
                t.append(x)
                mi.append(y)
                mp.append(z)
            if (i == 1):
                if (j % 2 == 0):
                    mil.append(y)
                    mpl.append(z)
            if (i == 2):
                if (j % 4 == 0):
                    mill.append(y)
                    mpll.append(z)
            x = x1
            y = y1
            z = z1

        n *= 2
        x = xi
        y = yi
        z = zi
        h = (xf - x) / n

    qcmi = [(mil[r] - mi[r]) / (mill[r] - mil[r]) if mill[r] - mil[r] != 0 else 0 for r in range(len(t))]
    qcmp = [(mpl[r] - mp[r]) / (mpll[r] - mpl[r]) if mpll[r] - mpl[r] != 0 else 0 for r in range(len(t))]
    error_mi = [(mill[r]-mil[r]) for r in range(len(t))]
    error_mp = [(mpll[r]-mpl[r]) for r in range(len(t))]
    print(mi)
    print(mil)
    print(mill)
    print(mp)
    print(mpl)
    print(mpll)
    return (t, mi, mp, qcmi, qcmp,error_mi,error_mp)

'''
@brief runge kutta 2's system of differential equations solver

@param x x's initial guess
@param y y's initial guess
@param z z's initial guess
@param xf final x to calculate
@param n number of iterations 

@return the calculated times and their respective mi, mp, qc of mi, qc of mp, error of mi and error of mp
'''
def runge_kutta_2(x,y,z,xf,n):
    xi = x
    yi = y
    zi = z
    t = []
    mi = []
    mil = []
    mill = []
    mp = []
    mpl = []
    mpll = []
    h = (xf-x)/n
    for i in range(3):
        for j in range(n):
            dy1 = f1(x,y,z)
            dz1 = f2(x,y,z)
            dy1a = f1(x+h/2,y+(h*dy1)/2,z+(h*dz1)/2)
            dz1a = f2(x+h/2,y+(h*dy1)/2,z+(h*dz1)/2)
            x1 = x + h
            y1 = y + dy1a*h
            z1 = z + dz1a*h
            if(i == 0):
                t.append(x)
                mi.append(y)
                mp.append(z)
            if(i == 1):
                if(j%2 == 0):
                    mil.append(y)
                    mpl.append(z)
            if(i == 2):
                if(j%4 == 0):
                    mill.append(y)
                    mpll.append(z)
            x = x1
            y = y1
            z = z1

        n *= 2
        x = xi
        y = yi
        z = zi
        h = (xf-x)/n

    qcmi = [(mil[r] - mi[r])/(mill[r]-mil[r]) if mill[r]-mil[r] != 0 else 0 for r in range(len(t)) ]
    qcmp = [(mpl[r] - mp[r])/(mpll[r]-mpl[r]) if mpll[r]-mpl[r] != 0 else 0 for r in range(len(t)) ]
    qcmi = [(mil[r] - mi[r]) / (mill[r] - mil[r]) if mill[r] - mil[r] != 0 else 0 for r in range(len(t))]
    qcmp = [(mpl[r] - mp[r]) / (mpll[r] - mpl[r]) if mpll[r] - mpl[r] != 0 else 0 for r in range(len(t))]
    error_mi = [(mill[r]-mil[r]) for r in range(len(t))]
    error_mp = [(mpll[r]-mpl[r]) for r in range(len(t))]
    print(mi)
    print(mil)
    print(mill)
    print(mp)
    print(mpl)
    print(mpll)
    return (t, mi, mp, qcmi, qcmp,error_mi,error_mp)

''' 
@brief runge kutta 4's system of differential equations solver

@param x x's initial guess
@param y y's initial guess
@param z z's initial guess
@param xf final x to calculate
@param n number of iterations

@return the calculated times and their respective mi, mp, qc of mi, qc of mp, error of mi and error of mp
'''
def runge_kutta_4(x,y,z,xf,n):
    xi = x
    yi = y
    zi = z
    t = []
    mi = []
    mil = []
    mill = []
    mp = []
    mpl = []
    mpll = []
    h = (xf-x)/n
    for i in range(3):
        for j in range(n):
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
            if(i == 0):
                t.append(x)
                mi.append(y)
                mp.append(z)
            if(i == 1):
                if(j%2 == 0):
                    mil.append(y)
                    mpl.append(z)
            if(i == 2):
                if(j%4 == 0):
                    mill.append(y)
                    mpll.append(z)
            x = x1
            y = y1
            z = z1

        n *= 2
        x = xi
        y = yi
        z = zi
        h = (xf-x)/n

    qcmi = [(mil[r] - mi[r]) / (mill[r] - mil[r]) if mill[r] - mil[r] != 0 else 0 for r in range(len(t))]
    qcmp = [(mpl[r] - mp[r]) / (mpll[r] - mpl[r]) if mpll[r] - mpl[r] != 0 else 0 for r in range(len(t))]
    error_mi = [(mill[r]-mil[r]) for r in range(len(t))]
    error_mp = [(mpll[r]-mpl[r]) for r in range(len(t))]
    print(mi)
    print(mil)
    print(mill)
    print(mp)
    print(mpl)
    print(mpll)
    return (t, mi, mp, qcmi, qcmp,error_mi,error_mp)

'''
@brief main function, calls the ridders method and runge kutta 4's function
        Graphs the values obtained 
'''
if __name__ == '__main__':
    n = int(10000*150)
    ka = false_position_ridders_relative(0.02,0.03,g1)
    mi = 0
    mp = 0
    elapsed_time = 0
    qcplotmi = []
    qcplotmp = []
    errormi = []
    errormp = []
    miplot = []
    mpplot = []
    t = []
    for i in range(5):
        lasttime = i*86400
        tf = lasttime + 86400
        start_time = time.time()
        val = runge_kutta_4(lasttime, mi, mp, tf, n)
        elapsed_time += time.time() - start_time
        mi = val[1][-1]
        mp = val[2][-1]
        qcplotmi += val[3]
        qcplotmp += val[4]
        errormi += val[5]
        errormp += val[6]
        miplot += val[1]
        mpplot += val[2]
        t += val[0]


    plt.suptitle("Runge-Kutta's Method 4")
    plt.plot(t, miplot, 'g', label="mi")
    plt.plot(t, mpplot, 'b', label="mp")
    plt.xlabel('time(s)')
    plt.ylabel('mass(g)')
    plt.show()

    fig, ((ax1), (ax2)) = plt.subplots(2, 1)
    fig.suptitle("Runge-Kutta's Method 4")
    ax1.plot(t[1:], qcplotmi[1:], 'g')
    plt.xlabel('time(s)')
    plt.ylabel('mass(g)')
    ax1.plot(t[1:], qcplotmp[1:],'b')
    plt.xlabel('time(s)')
    plt.ylabel('mass(g)')
    ax2.plot(t[1:], errormi[1:], 'g')
    plt.xlabel('time(s)')
    plt.ylabel('mass(g)')
    ax2.plot(t[1:], errormp[1:], 'b')
    plt.xlabel('time(s)')
    plt.ylabel('mass(g)')

    ax1.set_ylim(-25,25)
    k = True
    for ax in fig.get_axes():
        if(k):
            ax.set(xlabel='time(s)', ylabel='qc')
            k = False
        else:
            ax.set(xlabel='time(s)', ylabel='err')


    for ax in fig.get_axes():
        ax.label_outer()

    plt.show()
    lasttime = tf
    print(elapsed_time)

    #print(mi)
    #print(mp)
    #plt.scatter(t, mi)

    #plt.scatter(t, mp)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
