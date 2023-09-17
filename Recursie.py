#Catalan Getallen - Done

Cn = 1
n = 1

f = lambda x, Cn: ((4*(x) + 2)/(x + 2))*Cn

def catalan(i, Cn = Cn, n = n):
    if i == 0:
        return Cn
    if i < 0:
        return -1 
    if i == n:
        return Cn
    Cn = f(n, Cn)
    n += 1
    return(catalan(i, Cn = Cn, n = n))

print(catalan(0))
print(catalan(31))

#Negatief Getal - Done

def negatief(l_neg, n = 0):
    if n > len(l_neg)-1:
        return 0
    if l_neg[n] < 0:
        return l_neg[n]
    return(negatief(l_neg, n = n+1))

print(negatief([]))

#Karakters Tellen - Done

def telKarakters(s, c, i = 0, n = 0):
    if i > len(s)-1:
        return n
    if s[i] == c:
        n += 1
    return telKarakters(s, c, i = i+1, n = n)

print(telKarakters('', 'C'))

#Palindroom - Done

def isPalindroom(s, i = 0, n = 0):
    if i == 0:
        n = round(len(s)/2)
    if i >= n or len(s) == 0:
        return True
    if s[i] != s[-(i+1)]:
        return False
    i += 1
    return isPalindroom(s, i = i, n = n)

print(isPalindroom(''))

#Drop out - Done

def drop_out(l_dropout, i = 0, output = None):
    if output == None:
        output = []
    output.append(l_dropout[:i]+l_dropout[i+1:])
    if i >= len(l_dropout)-1:
        return output
    i += 1
    return(drop_out(l_dropout, i = i, output = output))

print(drop_out(['A', 'B', 'C', 'A', 'B', 'C']))

#Motieven Tellen - WIP

def telMotief():
    return 0

#geisoleerde cijfers

def geisoleerde_cijfers(string, n = 0, i = 1):
    if i >= len(string)-1 or len(string) == 0:
        return n
    if i == 1:
        if string[0].isdigit() and not string[1].isdigit():
            n += 1
        if string[-1].isdigit() and not string[-2].isdigit():
            n += 1
    if string[i].isdigit() and not (string[i-1].isdigit() or string[i+1].isdigit()):
        n += 1
    i += 1
    return geisoleerde_cijfers(string, n = n, i = i)

print(geisoleerde_cijfers("1aaas5asdfasf645165sa1f6a5s1fd65as154a"))

#Hakken - Done

import math

def hakken(s, n, l = None, i = 0):
    if l == None:
        l = []
    if i >= math.ceil(len(s)/n):
        return l
    l.append(s[i*n:(i+1)*n])
    i += 1
    return hakken(s, n, l = l, i = i)

hakken('abcdefghijklm', 5)

#Maken van Bins - Done

def maak_bins(a, b, N, i = 0, l = None, intS = 0):
    if l == None:
        l = []
        intS = (b - a)/N
    if i >= N:
        return l
    l.append((i*intS + a,(i+1)*intS + a))
    i += 1
    return maak_bins(a, b, N, i = i, l = l, intS = intS)

print(maak_bins(0.0, 10.0, 5))

#Plateau - WIP

def plateau(l, p, i, n = 0):
    


    return plateau(l, p, i, n = n)

#Intervallijst - Done

def interval_lijst(x, l, i = 0, l2 = None):
    if l2 == None:
        l2 = []
    if i >= len(l):
        return l2
    if (x > l[i][0]) and (x < l[i][1]):
        l2.append(i)
    i += 1
    return interval_lijst(x, l, i = i, l2 = l2)

l = [(1.0, 5.0), (7.0, 12.0), (4.0, 9.0), (5.0, 20.0)]
print(interval_lijst(8.0, l)) #[1, 2, 3]

#Prefix Lijst - Done

def prefix_lijst(x, l, i = 0):
    if i >= len(l):
        return l
    l[i].insert(0, x)
    i += 1
    return prefix_lijst(x, l, i = i)

l1 = [[4, 4], [1, 1], [1, 2, 3]]
print(prefix_lijst(5, l1))

#Begrenzing van Lijsten

def begrens(l, x, i = 0):

    return begrens(l, x, i = i)