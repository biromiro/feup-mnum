# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 19:59:26 2021

@author: exame
"""


def gauss_seidel(A,X0,B,n):
    X = [0,0,0,0]
    for _ in range(n):
        for i in range(len(X0)):
            X[i] = (1/A[i][i])*(B[i] - sum([A[i][j]*X[j] if j<i else 0 for j in range(len(X0))])
                                -sum([A[i][j]*X0[j] if j>i else 0 for j in range(len(X0))]))
        X0[0] = X[0]
        X0[1] = X[1]
        X0[2] = X[2]
        X0[3] = X[3]
    return X

print(gauss_seidel([[6,0.5,3,0.25],[1.2,3,0.25,0.2],[-1,0.25,4,2],[2,4,1,8]], [-0.81959,1.40167,2.15095,0.11019],[2.5,3.8,10,7], 2))
