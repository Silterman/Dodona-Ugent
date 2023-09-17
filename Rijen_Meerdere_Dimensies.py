#Sommen van Rijen

import numpy as np

def som_rij_kolom(x):
    s = np.zeros((len(x)+1,len(x[0])+1))

    for j in range(len(x)):
        for i in range(len(x[0])):
            s[j][i] = x[j][i]
        s[j][len(x[0])] = sum(s[j])
    
    for i in range(len(s[0])):
        n = 0
        for j in range(len(s)):
            n += s[j][i]
        s[-1][i] = n

    return s

som_rij_kolom(np.array([[ 0,  1,  2,  3,  4], [10, 11, 12, 13, 14], [20, 21, 22, 23, 24], [30, 31, 32, 33, 34]]))

#Geldstukken

def schat(x, m, n):
    
    return

r = np.array([[False, False, True, True, False],[True, False, False, False, False], [True, True, False, False, False],[False, False, False, False, False],[False, True, False, True, True],[False, True, False, True, True]]) 
schat(r, 2, 2)

#Diagonalen

import numpy as np

def diag_tabel(N):
    t = np.ones((N,N))
    for i in range(N):
        for j in range(N):
            try:
                t[j+i][j] += i
                t[j][j+i] += i
            except:
                continue
    return t.astype(int)

diag_tabel(3)

#Grootste 4-norm:

import numpy as np

def grootste4_eerst(x, l = None):
    if l == None:
        l = []
    y = np.zeros((len(x),len(x[0])))
    for i in x:
        s = 0
        for j in i:
            s += j**4
        l.append(s)
    o = (l.index(max(l)), 0)
    y[0] = x[l.index(max(l))]; y[l.index(max(l))] = x[0]
    for i in range(len(x)):
        if i in o:
            continue
        y[i] = x[i]
    return y

a = [[0., 1., 2., 3., 4.], [1. ,2. ,3. ,4. ,5.], [2. ,3. ,4. ,5. ,6.], [3. ,4. ,5. ,6. ,7.]]
grootste4_eerst(a)