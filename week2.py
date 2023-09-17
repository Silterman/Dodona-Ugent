#ISBN

x = input()
while x != "stop":
    n = 0
    if x[-1] == "X":
        code = 10
    else:
        code = int(x[-1])
    for i in range(9):
        n += (i+1)*int(x[i])
    if n%11 == code:
        print("OK")
    else:
        print("FOUT")
    x = input()

#Dagboek voor Stella

gecodeerd = str(input())
zin = ""
n = 0

for letter in gecodeerd:
    if not letter.isalpha():
        zin += letter
        continue
    if n%2 == 0:
        zin += letter
    n += 1

print(zin)

#Pi-ramidale constanten

a = str(input())
a = a.replace(".", "")
a = a.replace("-", "")
if a[0] == "0":
    a = a[1:]
n = int(input())
pos = 0
output = ""

for i in range(1,1+n):
    regel = "" #met een lege regel beginnen

    for _ in range(i): #elk apart getal in de komende regel stelt een _ voor
        x = 0

        for _ in range(i):
            x += int(a[pos])
            pos += 1

        regel += str(x) + " "

    output += regel[:-1]
    if i != n:
        output += "\n" #telkens een nieuwe regel opstarten, behalve bij de laatste regel

print(output)

#Een speld in een hooiberg

woord = str(input())
woord_normaal = woord.lower()
woord_reverse = woord_normaal[::-1]
n = int(input())

for i in range(n):
    regel = str(input()).lower()
    try:
        if woord_normaal in regel:
            print(f"{woord} staat op rij {i} en kolom {regel.index(woord_normaal)}")
            break
        if woord_reverse in regel:
            print(f"{woord} staat op rij {i} en kolom {regel.index(woord_reverse)}")
            break
    except ValueError:
        pass
    if i == n-1:
        print(f"{woord} werd niet gevonden")

#ISBN

def isISBN(x):    
    if not isinstance(x, str):
        return False
    try:
        n = int(x[:9])
    except ValueError:
        return False

    n = 0
    if x[-1] == "X":
        code = 10
    else:
        code = int(x[-1])

    for i in range(1, 10):
        n += i*int(x[i-1])

    if n%11 == code:
        return True
    return False

#Wimbledon

import math

def decodeer(s, opl=""):
    for i in range(math.floor(len(s)/2)):
        opl += s[i]
        opl += s[-(i+1)]
    if (len(s)/2)%1 != 0:
        opl += s[-math.floor(len(s)/2)-1]
    return opl

def codeer(s, begin="", einde=""):
    for i in range(0,len(s)-1,2):
        begin += s[i]
        einde += s[i+1]
    if len(s)%2 != 0:
        begin += s[-1]
    return begin+einde[::-1]

#ergonomie

def positie(letter, a="ABCDEFGHIJKLM", b="NOPQRSTUVWXYZ"):
    letter = letter.upper()
    if letter in a:
        return (0, a.index(letter))
    return (1, b.index(letter))

def verschuiving(letter1, letter2):
    co1 = positie(letter1)
    co2 = positie(letter2)
    return abs(co1[0]-co2[0]) + abs(co1[1]-co2[1])

def ergonomie(woord):
    dist = 0
    for i in range(len(woord)-1):
        dist += verschuiving(woord[i], woord[i+1])
    return dist

#Camachogetallen

def camachoterm(n, p, x=0):
    n = str(n)
    for i in n:
        x+=int(i)**p
    return x

def camachosom(n, som=0):
    for i in range(1, len(str(n))+1):
        som += camachoterm(n, i)
    return som

def iscamacho(n):
    if camachosom(n) == n:
        return True
    return False

def volgende_camacho(n):
    while not iscamacho(n+1):
        n += 1
    return n+1