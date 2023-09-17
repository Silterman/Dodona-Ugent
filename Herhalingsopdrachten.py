#Positief - Negatief

def positiefNegatief(l):
    s = []
    for i in l:
        if i < 0:
            s.append(i)
    for i in l:
        if i >= 0:
            s.append(i)
    return s

positiefNegatief([1, -2, 3, -4, 5, -6])

#Gelijke macht

def gelijkeMacht(n, m):
    l = []
    for i in range(m-1):
        for j in range(i+1, m, 1):
            if i**n % m == j**n % m:
                l.append((i, j))
    return l

gelijkeMacht(3, 7)

#Aangeschakeld

import numpy as np

def aangeschakeld(x, a):
    s = np.clip(x, None, a+1)
    l = np.where(s == a+1)[0]
    return (l[0],l[-1])

aangeschakeld(np.array([1, 1, 2, 1, 1, 3, 2, 1, 4, 6, 8, 8, 9, 9, 9, 10, 9, 8, 7, 6, 6, 6, 5, 2, 1, 2, 1]), 5)

#Puzzelsjabloon

def isMogelijk(sjabloon, opl):
    if len(sjabloon) != len(opl):
        return False
    for i in range(len(sjabloon)):
        if sjabloon[i] == "?" or sjabloon[i] == opl[i]:
            continue
        else:
            return False
    return True

isMogelijk('AA???B?C', 'AAaaaBbC')
isMogelijk('AA???B?C', 'AAaaaBbD')

#Tekstafstand

def afstand(a, b, x = 0):
    x += abs(len(a) - len(b))
    if len(b) > len(a):
        x1 = b; x2 = a
    else:
        x1 = a; x2 = b
    for i in range(len(x2)):
        if x1[i] != x2[i]:
            x += 1
    return x

afstand('AAAAA', 'AAAAA')
afstand('AAABBB', 'AABB')

#Afstand in Manhattan

import numpy as np

def manhattan(a, b, x = 0):
    if len(a) != len(b):
        return -1.0
    for i in range(len(a)):
        x += np.abs(a[i] - b[i])
    return x

manhattan(np.array([1.0, 2.0]), np.array([-1.0, -2.0]))

#Grens

