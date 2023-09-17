#isbn

def isISBN10(isbn, l=None, xSum = 0, xExpectedSum = None):
    if l is None:
        l = []

    if len(isbn) != 10:
        return False

    for i in isbn:
        if i.isdigit() or i == "X":
            l.append(i)
        elif i != "-":
            return False

    if l[-1] == "X":
        xExpectedSum = 10
    else:
        xExpectedSum = int(l[-1])

    for i in range(1, 10):
        xSum += i*int(l[i-1])

    return xSum%11 == xExpectedSum

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

def isISBN(isbn, isbn13=True):
    if not isinstance(isbn, str):
        return False
    if isbn13 is None:
        if len(isbn) == 10:
            isbn13 = False
        else:
            isbn13 = True
    if not isbn13:
        return isISBN10(isbn)
    return isISBN13(isbn)

def zijnISBN(listISBN,isbn13=None ,listISBNResult=None):
    if listISBNResult is None:
        listISBNResult = []
    for i in listISBN:
        listISBNResult.append(isISBN(i, isbn13))
    return listISBNResult

#Zelfbeschrijvende Reeksen

def cijferfrequentie(strFreqNumb, l=None):
    if l is None:
        l = [0]*10
    for i in range(10):
        l[i] = strFreqNumb.count(str(i))
    return tuple(l)

def beschrijving(listFreqNumb, strFreqNumb=""):
    for i, val in enumerate(listFreqNumb):
        if val == 0:
            strFreqNumb += str(i) + " "
            continue
        strFreqNumb += str(val) + str(i) + " "
    return strFreqNumb[:-1]

def iszelfbeschrijvend(tupleSerStrFreq, listSerListFreq=None, currentStr=""):
    if listSerListFreq is None:
        listSerListFreq = []
    for i in tupleSerStrFreq:
        listSerListFreq.append(cijferfrequentie(i))
    for i in range(len(listSerListFreq)):
        currentStr += tupleSerStrFreq[i]
        currentStrFreq = cijferfrequentie(currentStr)
        if beschrijving(currentStrFreq) != tupleSerStrFreq[i]:
            return False
    return True

def iszelfbeschrijvend_2(*arg):
    l = []
    for i in arg:
        l.append(arg)
    while None in l:
        l.remove(None)
    if len(l) == 0:
        return True
    if len(l) > 5:
        return False
    return iszelfbeschrijvend(tuple(l))

#Werkelijkheid en Fictie

import string

alfToNumb={'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7,'I': 8,'J': 9,'K': 10,'L': 11,'M': 12,
'N': 13,'O': 14,'P': 15,'Q': 16,'R': 17,'S': 18,'T': 19,'U': 20,'V': 21,'W': 22,'X': 23,'Y': 24,'Z': 25}
numbToAlf={0: 'A',1: 'B',2: 'C',3: 'D',4: 'E',5: 'F',6: 'G',7: 'H',8: 'I',9: 'J',10: 'K',11: 'L',12: 'M',
13: 'N',14: 'O',15: 'P',16: 'Q',17: 'R',18: 'S',19: 'T',20: 'U',21: 'V',22: 'W',23: 'X',24: 'Y',25: 'Z'}

def codeer_letter(let, letCod="A"):
    global alfToNumb, numbToAlf
    letNumb = alfToNumb[let.upper()]
    letCodNumb = alfToNumb[letCod.upper()]
    if let.islower():
        return numbToAlf[(letNumb+letCodNumb)%26].lower()
    return numbToAlf[(letNumb+letCodNumb)%26]

def decodeer_letter(let, letCod="A"):
    global alfToNumb, numbToAlf
    letNumb = alfToNumb[let.upper()]
    letCodNumb = alfToNumb[letCod.upper()]
    if let.islower():
        return numbToAlf[(letNumb-letCodNumb)%26].lower()
    return numbToAlf[(letNumb-letCodNumb)%26]

def codeer(sentence, result=""):
    for i, val in enumerate(sentence):
        if val in string.ascii_letters:
            keyWord = sentence[i-1]
            n = 2
            while keyWord not in string.ascii_letters:
                if n > i:
                    keyWord = "A"
                    break
                keyWord = sentence[i-n]
                n += 1
            try:
                result += codeer_letter(val, keyWord)
            except:
                result += codeer_letter(val)
        else:
            result += val
    return result

def decodeer(sentence, result=""):
    for i, val in enumerate(sentence):
        if val in string.ascii_letters:
            try:
                keyWord = result[i-1]
            except:
                result += decodeer_letter(val)
                continue
            n = 2
            while keyWord not in string.ascii_letters:
                if n > i:
                    keyWord = "A"
                    break
                keyWord = result[i-n]
                n += 1
            try:
                result += decodeer_letter(val, keyWord)
            except: 
                result += decodeer_letter(val)
        else:
            result += val
    return result

print(codeer('Henry Walton Jones Jr.'))
print(decodeer("Hlrep Uwlehb Wxbrw Ba."))

#isbn

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

def overzicht(listISBNCodes):
    landCodes=[0]*8 #EN,FR,DE,JP,RU,CN,ETC,F
    for i in listISBNCodes:
        if isISBN13(i) and i[:3] in ["978", "979"]:
            if i[3] in ["0", "1"]:
                landCodes[0] += 1
            elif i[3] in ["2"]:
                landCodes[1] += 1
            elif i[3] in ["3"]:
                landCodes[2] += 1
            elif i[3] in ["4"]:
                landCodes[3] += 1
            elif i[3] in ["5"]:
                landCodes[4] += 1
            elif i[3] in ["7"]:
                landCodes[5] += 1
            elif i[3] in ["6", "8", "9"]:
                landCodes[6] += 1
        else:
            landCodes[-1] += 1

    print("Engelstalige landen: " + str(landCodes[0]))
    print("Franstalige landen: " + str(landCodes[1]))
    print("Duitstalige landen: " + str(landCodes[2]))
    print("Japan: " + str(landCodes[3]))
    print("Russischtalige landen: " + str(landCodes[4]))
    print("China: " + str(landCodes[5]))
    print("Overige landen: " + str(landCodes[6]))
    print("Fouten: "  +  str(landCodes[7]))

#Halsketting

import itertools
import string

def rotatie(word, rotFactor, tempList=None):
    if tempList is None:
        tempList = []
    for i in range(len(word)):
        tempList.append(word[(i+rotFactor)%len(word)])
    return "".join(tempList)

def rotaties(word, listRot=None):
    if listRot is None:
        listRot = []
    for i in range(len(word)):
        listRot.append(rotatie(word, i).upper())
    return set(listRot)

def normaalvorm(word):
    return sorted(list(rotaties(word)))[0]

def halskettingen(k, n):
    l = []
    x = []
    keyword = string.ascii_uppercase[:k]
    s = itertools.product(keyword, repeat=n)
    for i in s:
        l.append("".join(i))
    for i in l:
        x.append(normaalvorm(i))
    return len(set(x))

#Kangoeroe

def kangoeroe(parentWord, childWord, n=0):
    for i in parentWord.lower():
        if i == childWord[n].lower():
            n += 1
            if n == len(childWord):
                return True
    return False

def jongen(parentWord, listChildWords, listFoundChildWords=None):
    if listFoundChildWords is None:
        listFoundChildWords = []
    for i in listChildWords:
        if kangoeroe(parentWord, i):
            listFoundChildWords.append(i)
    return set(listFoundChildWords)

kangoeroe('BLOSSOM', 'bloom')
jongen('ALONE', {'lone', 'one', 'only', 'solo', 'unaccompanied'})

#Om de hoek

def isveelhoek(puzzleWordList):
    if isinstance(puzzleWordList, set):
        return False
    if len(puzzleWordList) < 3:
        return False
    for i in puzzleWordList:
        if not isinstance(i, str):
            return False
        if not i.isupper() or not i.isalpha():
            return False
    lenPuzzle = len(puzzleWordList[0])
    for i in range(1, len(puzzleWordList)):
        if len(puzzleWordList[i]) != lenPuzzle:
            return False
    return True

def oplossing(puzzleWordList, start=0, wijzerzin=True, strWordList="", solution=""):
    distLetters = len(puzzleWordList)
    wordCollectionList=[]
    for i in range(distLetters):
        strWordList += puzzleWordList[(start+i)%distLetters]
    for i in range(0, len(strWordList), distLetters):
        wordCollectionList.append(strWordList[i])
    if not wijzerzin:
        for i in range(len(wordCollectionList)):
            solution += wordCollectionList[((-i)*2)%len(wordCollectionList)]
        return solution
    
    return solution

print(oplossing(['DRIEHOEK', 'KEERMUUR', 'NACHTBUS']))
oplossing(('DAMESROMANS', 'BEGINSCHERM', 'ONTSPANNEND', 'ERONDERDOOR', 'FAMILIEGRAF'), start=3, wijzerzin=False)