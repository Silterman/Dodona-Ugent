#ISBN

def isISBN13(isbn, listNumb=None, o=0, e=0):
    if listNumb is None:
        listNumb = []

    if len(isbn) != 13:
        return False

    for i in isbn:
        listNumb.append(i)
    for i in range(0, 11, 2):
        o += int(listNumb[i])
        e += int(listNumb[i+1])

    return int(listNumb[12]) == (10-(o+3*e)%10)%10

url = "https://pythia.ugent.be/pythia-share/exercises/isbn9/books.php?isbn="

import string

def print_boek_info(boekcode):
    if not isISBN13(boekcode):
        print("Foutieve ISBN-13 code")
        return

    from urllib.request import urlopen
    global url
    
    localUrl = urlopen(url + str(boekcode))
    

    for line in localUrl:
        lineConv = line.decode("utf-8")
        if lineConv.startswith("<Title>"):
            print(f"Titel: {lineConv[7:-9]}")
        elif lineConv.startswith("<AuthorsText>"):
            cutoffEnd = -18
            while lineConv[cutoffEnd] in string.ascii_letters:
                cutoffEnd += 1
            print(f"Auteurs: {lineConv[13:cutoffEnd]}")
        elif lineConv.startswith("<PublisherText"):
            cutoff = lineConv.index(">")+1
            print(f"Uitgever: {lineConv[cutoff:-17]}")

print(print_boek_info('9780136110675'))

#Rorshachtest

def rorschach(docName, docNameRor=None, tempList=None):
    if tempList is None:
        tempList = []
    openDoc = open(docName, "r")
    for line in openDoc:
        if line[-1] == "\n":
            curLine = line[:-1]
        else:
            curLine = line
        tempList.append(curLine+curLine[::-1])
    if docNameRor is None:
        for i in tempList:
            print(i)
    else:
        openWriteDoc = open(docNameRor, "w")
        for i in tempList:
            openWriteDoc.write(i+"\n")

#BADA55

def leet2letter(docName, trlDict=None):
    if trlDict is None:
        trlDict = {}
    
    openDoc = open(docName, "r")
    for line in openDoc:
        tempList = []
        number = line[0]
        cutOff = line.index(">")+2
        cutOffEnd = len(line)
        if line[-1] == "\n":
            cutOffEnd = -1
        letters = line[cutOff:cutOffEnd]
        for i in letters:
            tempList.append(i.upper())
        trlDict.update({number.upper():set(tempList)})

    return trlDict

def letter2leet(trlDict, trlDictLetters=None):
    if trlDictLetters is None:
        trlDictLetters = {}
    
    for i in trlDict:
        for j in trlDict[i]:
            trlDictLetters.update({j:i})
    
    return trlDictLetters

def leetspeak(word, trlDictLetters, tempList=None, output=""):
    if tempList is None:
        tempList = []
    for i in word:
        tempList.append(i)
    for i in tempList:
        try:
            output += trlDictLetters[i.upper()]
        except:
            output += i.upper()
    return output

def ishexkleur(word):
    import re
    regex = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
    p = re.compile(regex)
    temp = re.search(p, word)
    if temp:
        return True
    return False

def kleur(word, trlDictLetters):
    leetWord = leetspeak(word, trlDictLetters)
    if not ishexkleur("#"+leetWord):
        raise AssertionError("ongeldige kleur")
    return "#" + leetWord

#Zweedse voorouders

def familieleden(docName, ):
    openDoc = open(docName, "r")
    pass

#Schiereiland

def landmass(docName, R=0, o=0, landList=None, coodList=None):
    if landList is None:
        landList=[]
        coodList=[]

    openDoc = open(docName, "r")

    for line in openDoc:
        if line[-1] == "\n":
            line = line[:-1]
        landList.append(list(line))

    xLen = len(landList[0])
    yLen = len(landList)

    for i in range(yLen):
        for j in range(xLen):
            if landList[i][j] == "S":
                o+=1
                try:
                    if landList[i-1][j] == "#" and (i-1, j) not in coodList and i-1>=0:
                        R +=1
                        coodList.append((i-1, j))
                except IndexError:
                    pass
                try:
                    if landList[i+1][j] == "#" and (i+1, j) not in coodList:
                        R +=1
                        coodList.append((i+1, j))
                except IndexError:
                    pass
                try:
                    if landList[i][j-1] == "#" and (i, j-1) not in coodList and j-1>=0:
                        R +=1
                        coodList.append((i, j-1))
                except IndexError:
                    pass
                try:
                    if landList[i][j+1] == "#" and (i, j+1) not in coodList:
                        R +=1
                        coodList.append((i, j+1))
                except IndexError:
                    pass

    return (R, o)

def landtype(docName, ratio=0.05):
    tup = landmass(docName)
    if tup[0] == 0:
        return "island"
    if tup[0]/tup[1] <= ratio:
        return "peninsula"
    return "mainland"

#Geen voor allen

import math

def euclidische_afstand(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def manhattanafstand(a, b):
    return float(abs(a[0]-b[0]) + abs(a[1]-b[1]))

def schaakbordafstand(a, b):
    return float(max(abs(a[0]-b[0]),abs(a[1]-b[1])))

def kudde(docName, fieldList=None, antiPosDict=None):
    if fieldList is None:
        fieldList = []
        antiPosDict = {}
    openDoc = open(docName, "r")
    for line in openDoc:
        if line[-1] == "\n":
            line = line[:-1]
        fieldList.append(list(line))
    
    lenY = len(fieldList)
    lenX = len(fieldList[0])

    for i in range(lenY):
        for j in range(lenX):
            if fieldList[i][j] != ".":
                antiPosDict.update({(i, j):fieldList[i][j]})

    return (lenY, lenX, antiPosDict)

def dichtste_antilopen(pos, antiPosDict, distList=None, afstand=euclidische_afstand, solution=None):
    if distList is None:
        distList = []
        solution = []
    for i in antiPosDict:
        distList.append((afstand(pos, i),antiPosDict[i]))
    minDist = sorted(distList)[0][0]

    for i in distList:
        if i[0] == minDist:
            solution.append(i[1])

    return set(solution)

def regios(docName, afstand=euclidische_afstand, fieldList=None, solution=""):
    if fieldList is None:
        fieldList = []
        antiPosDict = {}
    openDoc = open(docName, "r")
    for line in openDoc:
        if line[-1] == "\n":
            line = line[:-1]
        fieldList.append(list(line))

    lenY, lenX, antiPosDict = kudde(docName)

    for i in range(lenY):
        for j in range(lenX):
            if not fieldList[i][j].isupper():
                fieldList[i][j] = sorted(list(dichtste_antilopen((i, j), antiPosDict, afstand=afstand)))[0].lower()

    for i in fieldList:
        solution += "".join(i) + "\n"

    return solution[:-1]