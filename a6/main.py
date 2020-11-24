import math
import numpy

def f(x):
    return math.sin(x)/(x*x)

def getmatrixLandU(A,B):
    U = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    L = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        L[i][0] = A[i][0]
        U[i][i] = 1
    for i in range(len(A)):
        U[0][i] = A[0][i] / L[0][0]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if(i>=j):
                summmatrix = [(L[i][k] * U[k][j]) for k in range(j)]
                summ = sum(summmatrix)
                L[i][j] = A[i][j] - summ
            if (i < j):
                U[i][j] = (A[i][j] - sum([L[i][k] * U[k][j] for k in range(i)])) / L[i][i]
    return (L,U)

def getSolutionsSubstitute(A,B):
    A_np = numpy.array(A)
    B_np = numpy.array(B)
    sol = numpy.linalg.inv(A_np).dot(B)
    return sol.tolist()

def khaletsky_method(A,B):
    L, U = getmatrixLandU(A,B)

def integrationTrapezial(a,b,n):
    h = (b-a)/n
    return (h/2)*(f(a) + sum([2*f(a+i*h) for i in range(1,n)]) + f(b))

def integrationSimpson(a,b,n):
    h = (b - a) / n
    return (h/3)*(f(a) + sum([(2*f(a+i*h) if i%2==0 else 4*f(a+i*h)) for i in range(1,n)]) + f(b))

if __name__ == '__main__':
    A = [[1,1,1],[3,-1,2],[2,0,2]]
    B = [8,-1,5]
    L,U = getmatrixLandU(A,B)
    Y = getSolutionsSubstitute(L,B)
    X = getSolutionsSubstitute(U,Y)
    print(X)
    #print(integrationTrapezial(math.pi/2,math.pi,4))
    #print(integrationSimpson(math.pi/2,math.pi,4))
    #qcTrapz = (integrationTrapezial(math.pi,math.pi/2,8) - integrationTrapezial(math.pi,math.pi/2,4))/(integrationTrapezial(math.pi,math.pi/2,16) - integrationTrapezial(math.pi,math.pi/2,8))
    #qcSimpson = (integrationSimpson(math.pi,math.pi/2,16) - integrationSimpson(math.pi,math.pi/2,8))/(integrationSimpson(math.pi,math.pi/2,32) - integrationSimpson(math.pi,math.pi/2,16))
    #errorTrapz = (integrationTrapezial(math.pi,math.pi/2,16) - integrationTrapezial(math.pi,math.pi/2,8))/3
    #errorSimpson = (integrationSimpson(math.pi,math.pi/2,16) - integrationSimpson(math.pi,math.pi/2,8))/15
    #print(qcTrapz,errorTrapz)
    #print(qcSimpson,errorSimpson)
    