#ISBN

def isISBN(isbn, l=None, xSum = 0, xExpectedSum = None):
    if l is None:
        l = []

    if isbn[1] != "-" or isbn[6] != "-" or isbn[-2] != "-" or isbn.count("-") != 3:
        return False

    for i in isbn:
        if i.isdigit() or i == "X":
            l.append(i)
        elif i != "-":
            return False

    if len(l) != 10:
        return False

    if l[-1] == "X":
        xExpectedSum = 10
    else:
        xExpectedSum = int(l[-1])

    for i in range(1, 10):
        xSum += i*int(l[i-1])

    return xSum%11 == xExpectedSum

#Isogrammen

import string

def voorkomens(woord, alphabet=list(string.ascii_lowercase), countList=None):
    woord = woord.lower()
    if countList is None:
        countList = [0]*26
    for i in range(26):
        countList[i] = woord.count(alphabet[i])
    return countList

def isogram(woord):
    if max(voorkomens(woord)) <= 1:
        return True
    return False

def anagram(woord1, woord2):
    if voorkomens(woord1) == voorkomens(woord2):
        return True
    return False

#Heremietkreeften

def opeenvolgend(listUnsorted):
    listSorted = sorted(listUnsorted)
    for i in range(0, len(listSorted)-1):
        if listSorted[i] != listSorted[i+1] -1:
            return False
    return True

def goudlokje(listUnsorted,l=None):
    if opeenvolgend(listUnsorted):
        return None

    if len(listUnsorted) != len(set(listUnsorted)):
        return None

    if l is None:
        l = []
    
    listSorted = sorted(listUnsorted)
    for i in range(0, len(listSorted)-1):
        if listSorted[i] != listSorted[i+1] -1:
            if listSorted[i]+1 not in listSorted:
                l.append(listSorted[i]+1)

    if len(l) == 1:
        return l[0]

    return None

def verhuizen1(listUnsorted):
    if isinstance(listUnsorted, tuple):
        listUnsorted = list(listUnsorted)
    reqNumber = goudlokje(listUnsorted)
    if reqNumber is None:
        return listUnsorted
    listUnsorted.append(reqNumber)
    return listUnsorted

def verhuizen2(listUnsorted):
    if isinstance(listUnsorted, tuple):
        listUnsorted = list(listUnsorted)
    reqNumber = goudlokje(listUnsorted)
    if reqNumber is None:
        return None
    listUnsorted.append(reqNumber)

#Doemsdagklok

def klok(timeDeficit):
    if timeDeficit == 0:
        return "00:00"
    hoursDeficit = timeDeficit//60
    minuteDeficit = timeDeficit%60

    if minuteDeficit == 0:
        hoursDeficit -= 1
        minuteDeficit = 60

    hourTime = str(23-hoursDeficit)
    minuteTime = str(60-minuteDeficit)

    if len(minuteTime) == 1:
        minuteTime = "0" + minuteTime

    if len(hourTime) == 1:
        hourTime = "0" + hourTime

    return f"{hourTime}:{minuteTime}"

def verloop(timedList, sortedTuple=None):
    if sortedTuple is None:
        sortedTuple=[]
    unsortedList = timedList.split(",")
    for i in unsortedList:
        sortedTuple.append((int(i[:5]), klok(int(i[5:]))))
    return tuple(sortedTuple)

def dreiging(year, sortedTuple):
    for i in range(len(sortedTuple)):
        if sortedTuple[i][0] == year:
            return sortedTuple[i][1]
        if sortedTuple[i][0] > year:
            return sortedTuple[i-1][1]

#Woordrekenkunst

import string

def alfabet(unsortedString, unsortedList=None):
    if unsortedList is None:
        unsortedList = []
    for i in unsortedString:
        if i in string.ascii_letters:
            unsortedList.append(i)
    unsortedList = sorted(set(unsortedList))
    return "".join(unsortedList)

def getal(word, example, solution, result=""):
    for i in str(word):
        location = example.index(i)
        result += solution[location]
    try:
        return int(result)
    except ValueError:
        return result

def getallen(wordString, example, solution, wordList=None, results=None):
    if results is None:
        results = []
    if wordList is None:
        wordList = wordString.split(" + ")
    for i in wordList:
        results.append(getal(i, example, solution))
    return tuple(results) 
    
def woord(word, example, solution):
    return getal(word, solution, example)

def uitkomst(wordString, example, solution):
    numberList = getallen(wordString, example, solution)
    return woord(sum(numberList), example, solution)
    
def isoplossing(solution, unsortedString):
    tempString = unsortedString.replace("=", "+")
    stringAlphabet = alfabet(tempString)
    tempList = unsortedString.split(" = ")
    try:
        tempBool = uitkomst(tempList[0], stringAlphabet, solution)
    except:
        return False
    return tempBool == tempList[1]

#Open reading frames



#Dronken mier

def rooster(sizeN, directionString, layerList=None):
    if len(directionString) != sizeN**2:
        raise AssertionError("ongeldige argumenten") 
    if layerList is None:
        layerList = []
    directionString = list(directionString)
    for i in range(len(directionString)//sizeN):
        layerList.append(directionString[i*sizeN:(i+1)*sizeN])
    return layerList

def tekst(layerList, layerString=""):
    for StopCode, i in enumerate(layerList):
        for indexJ, j in enumerate(i):
            layerString += j
            if indexJ == len(i)-1:
                continue
            layerString += " "
        if StopCode == len(layerList)-1:
            break
        layerString += "\n"
    return layerString

def stap(layerList, posTuple):
    movementLib={"^":(0,-1), ">":(1, 0), "v":(0, 1), "<":(-1, 0)}
    movementList=["^", ">", "v", "<"]\
    
    posDirection = layerList[posTuple[0]][posTuple[1]]
    movement = movementLib[posDirection]
    tempPosList = [None]*2
    
    layerList[posTuple[0]][posTuple[1]] = movementList[(movementList.index(posDirection)+1)%4]

    for i in range(2):
        tempPosList[i] = posTuple[i] + movement[(i-1)%2]
        if tempPosList[i] >= len(layerList) or tempPosList[i] < 0:
            return posTuple
    return tuple(tempPosList)

def stappen(layerList, startPos=(3,0), posList=None):
    if posList is None:
        posList = []
    posList.append(startPos)
    if startPos == (0,3):
        return posList
    startPos = stap(layerList, startPos)
    return stappen(layerList, startPos, posList=posList)


vierkant = rooster(4, '>>>>^<^v^v^^>>v>')
print(tekst(vierkant))
stappen(vierkant)