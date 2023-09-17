#Normaliseren - Done

import numpy as np

def normaliseer(l):
    x_ma = max(l)
    x_mi = min(l)
    x = max([abs(x_mi), abs(x_ma)])
    for i in range(len(l)):
        l[i] = l[i]/x
    return l

normaliseer(np.linspace(-5, 5, 11))

#Gauss - Done

import numpy as np

def gauss(x, gem, spr):
    a = (1/(np.sqrt(2*np.pi)*spr))
    macht = -(x - gem)**2/(2*spr**2)
    return a*np.exp(macht)

gauss(0.0, 0.0, 1.0)
gauss(np.array([-5., -4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.,  5.]), 0.0, 1.0)

#Trapeziumrgel

def trapezium(f, a, b, N, L = []):
    l = np.zeros(N)
    B = b/N
    for i in range(N):
        l[i] = (round(i*B,1), round((i+1)*B,1))
    return l

trapezium(lambda x:2*x, 0, 1, 10)


#Dichtste buur

import numpy as np

def dichtsteBuur(x, v):
    f = lambda x,v: abs(x-v)
    x = f(x,v)
    minV = np.where(x == min(x))
    return minV[0][0]

dichtsteBuur(np.linspace(-5, 5, 11), 2.1)\

#Hoek tussen Vectoren - WIP

import numpy as np

def hoek(v1, v2):
    if len(v1) != len(v2):
        return -1
    x = 0
    for i in range(len(v1)-1):
        x += v1[i]*v2[i]
    return np.arccos(x/(abs(np.linalg.norm(v1))*abs(np.linalg.norm(v2))))

hoek(np.array([1, 1, 0]), np.array([1, 1, 1]))

#Voortschrijdend Gemiddelde

import numpy as np

def voortGem(l, n):
    l_t = np.zeros(len(l))
    for i in range(len(l)):
        t = l[max([i+1-n,0]):i+1]
        s = sum(t)/len(t)
        l_t[i] = s
    return l_t

voortGem([-10.0, -8.0, -6.0, -4.0, -2.0, 0.0, 2.0, 4.0, 6.0, 8.0, 10.0], 2)

#Lineaire Regressie

import numpy as np

def regressie(x, y, a1 = 0, a2 = 0, b = 0):
    Mx = sum(x)/len(x); My = sum(y)/len(y)
    for i,j in zip(x,y):
        a1 += (i-Mx)*(j-My); a2 += (i-Mx)**2
    a = a1/a2
    b = My - a*Mx
    return (a, b)

regressie([-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0], [-7.0, -5.0, -3.0, -1.0, 1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 13.0])
