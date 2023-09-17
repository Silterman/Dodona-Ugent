#Codon

def genetische_code(docName, codonDict=None):
    if codonDict is None:
        codonDict={}
    openDoc = open(docName, "r")
    for line in openDoc:
        if line.startswith("Codon"):
            continue
        codonDict.update({line[:3].upper().replace("U", "T"):line[-2:-1].upper()})
    return codonDict

def omgekeerde_genetische_code(codonDict, codonDictRev=None):
    if codonDictRev is None:
        codonDictRev={}
        ListCodes=[]
        for i in codonDict:
            if not codonDict[i] in ListCodes:
                ListCodes.append(codonDict[i].upper())
        for i in ListCodes:
            tempList=[]
            for j in codonDict:
                if codonDict[j] == i:
                    tempList.append(j)
            codonDictRev.update({i:set(tempList)})
    return codonDictRev

def synoniemen(codon, codonDict, RNA=None):
    if RNA is None:
        if "U" in codon.upper():
            RNA=True
        else:
            RNA=False
    codon = codon.upper().replace("U", "T")
    revCodonDict = omgekeerde_genetische_code(codonDict)
    for i in revCodonDict:
        if codon in revCodonDict[i]:
            returnCod = list(revCodonDict[i])
    if RNA:
        for i, val in enumerate(returnCod):
            returnCod[i] = val.replace("T", "U")
    return set(returnCod)

def codonoptimalisatie(listCodons):
    listCodons = sorted(listCodons)
    templist=[]
    for i in listCodons:
        templist.append(i.upper().count("C")+i.upper().count("G"))
    maxnumb = templist.index(max(templist))
    return listCodons[maxnumb]

def peptideoptimalisatie(codonString, codonDict, RNA=None):
    tempList = []
    for i in range(0, len(codonString), 3):
        tempList.append(codonString[i:i+3])
    for i, val in enumerate(tempList):
        tempList[i] = codonoptimalisatie(synoniemen(val, codonDict, RNA))
    return "".join(tempList)

code = genetische_code('genetische_code.txt')
peptideoptimalisatie('GCTCAACCTAACGGCAAGAAGGAGAGGGAATCTACGTAC', code, False)

#Digrafud

import string
#import numpy #only needed to create visual representation of the intersection of our two matrices

class Rooster:
    def __init__(self, keyword):
        tempStr = ""
        for i in keyword:
            if not i.upper() in tempStr:
                tempStr += i.upper()
        if not " " in keyword:
            tempStr += " "
        for i in string.ascii_uppercase:
            if not i in tempStr:
                tempStr += i
        self.rooster = [list(tempStr[:9]), list(tempStr[9:18]), list(tempStr[18:])]
    def __str__(self):
        string = ""
        for i in self.rooster:
            string += "".join(i) + "\n"
        return string[:-1]
    def positie(self, keyLetter):
        for i in range(3):
            for j in range(9):
                if self.rooster[i][j] == keyLetter.upper():
                    return (i, j)
    def karakter(self, x, y):
        return self.rooster[x][y]
        
class Digrafid:
    def __init__(self, keyword1, keyword2):
        self.keyword1 = Rooster(keyword1)
        self.keyword2 = Rooster(keyword2)
        self.temp = [[0,1,2],[3,4,5],[6,7,8]]
        #self.keyword2Transpose = numpy.array(self.keyword2).T.tolist() #transpose the list for visual representation
    def triplet(self, letters):
        a = self.keyword1.positie(letters[0].upper())
        c = self.keyword2.positie(letters[1].upper())
        return (a[1], self.temp[a[0]][c[0]], c[1])
    def digraaf(self, a, b, c):
        for i in range(3):
            for j in range(3):
                if self.temp[i][j] == b:
                    coodMid = (i, j)
        return self.keyword1.rooster[coodMid[0]][a] + self.keyword2.rooster[coodMid[1]][c]
    def codeer(self, sent):
        tempList = []
        str = ""
        while len(sent)%6 != 0:
            sent += "X"
        for i in range(0, len(sent), 2):
            tempList.append(sent[i:i+2].upper())
        for i in range(0, len(tempList),3): #creates the list of 3x3 matrices needed to "translate" the triplets of digrafids, very long I know, can probably be reduced in size just like this comment :)
            tripList = [(self.triplet(tempList[i])[0], self.triplet(tempList[i+1])[0], self.triplet(tempList[i+2])[0]), (self.triplet(tempList[i])[1], self.triplet(tempList[i+1])[1], self.triplet(tempList[i+2])[1]), (self.triplet(tempList[i])[2], self.triplet(tempList[i+1])[2], self.triplet(tempList[i+2])[2])]
            for i in tripList:
                str += self.digraaf(i[0], i[1], i[2])
        return str
    def decodeer(self, sent):
        return self.codeer(sent)


digrafid = Digrafid('Anakin Skywalker', 'Padme Amidala')
#print(digrafid.keyword1.rooster)
#print(digrafid.keyword2.rooster)
digrafid.triplet("OM")
digrafid.digraaf(5, 1, 7)
print(digrafid.codeer('Someday I will be the most powerful Jedi ever'))
print(digrafid.decodeer("SEOMHFGLAPFXJCAMXW PHLCYFFKBK EZFRE JJCPTEYOGZTI"))