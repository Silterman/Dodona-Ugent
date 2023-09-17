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

class ISBN13:
    def __init__(self, isbn, landcode=1):
        self.isbn = str(isbn)
        if landcode not in [1, 2, 3, 4, 5]:
            raise AssertionError("ongeldige ISBN code")
        else:
            self.landcode = landcode
    def __str__(self):
        return f"{self.isbn[:3]}-{self.isbn[3:3+self.landcode]}-{self.isbn[3+self.landcode:-1]}-{self.isbn[-1]}"
    def __repr__(self):
        return "ISBN13(%s, %d)"%(self.isbn, self.landcode)
    def alsISBN10(self):
        if self.isbn[:3] != "978" or not self.isgeldig():
            return

        code = self.isbn[3:-1]

        controle = sum((i+1) * int(code[i]) for i in range(9)) % 11

        if controle == 10:
            controle = "X"
        
        return f"{self.isbn[3:3+self.landcode]}-{self.isbn[3+self.landcode:-1]}-{controle}"
    def isgeldig(self):
        return isISBN13(self.isbn)

#Mad libs

import random

class MadLibs:
    def __init__(self, woordenschat=None):
        if woordenschat is None:
            woordenschat={}
        self.woordenschat = woordenschat
    def leren(self, cat, word):
        if not cat in self.woordenschat:
            if isinstance(word, str):
                self.woordenschat.update({cat:{word.lower()}})
            else:
                tempList1 = []
                for i in word:
                    tempList1.append(i.lower())
                self.woordenschat.update({cat:set(tempList1)})
            return
        tempList = list(self.woordenschat[cat])
        if isinstance(word, str):
            tempList.append(word.lower())
        else:
            for i in word:
                tempList.append(i.lower())
        self.woordenschat.update({cat:set(tempList)})
        return
    def suggereren(self, cat):
        if cat.lower() not in self.woordenschat:
            raise AssertionError("onbekende categorie")
        if cat.islower():
            return random.choice(list(self.woordenschat[cat]))
        if cat.isupper():
            return random.choice(list(self.woordenschat[cat.lower()])).upper()
        return random.choice(list(self.woordenschat[cat.lower()])).capitalize()
    def invullen(self, sent):
        tempList = sent.split("_")
        return tempList

#       tempList = []
#       startIndex = 1
#       endIndex = 0
#       for i, val in enumerate(sent):
#           if startIndex <= endIndex:
#               startIndex +=1
#               continue
#           if val == "_":
#               startIndex = i
#               tempList.append(sent[endIndex:startIndex])
#               for j in range(i, len(sent)):
#                   if sent[j] == "_":
#                       endIndex = j
#                       tempList.append(sent[startIndex:endIndex])
#       return "".join(tempList)

madlib01 = MadLibs()
madlib01.leren('skill', {'physics', 'programming', 'mathematics', 'cars', 'imagination', 'logic'})
madlib01.woordenschat
madlib01.invullen('_Skill_ will get you from A to Z; _skill_ will get you everywhere.')

#Str8ts

#Maanrekenen

class Maan():
    def __init__(self, numb):
        try:
            self.numb=int(numb)
        except:
            raise AssertionError("ongeldige waarde")
        if numb < 0:
            raise AssertionError("ongeldige waarde")
    def __repr__(self):
        return f"Maan({self.numb})"
    def __str__(self):
        return f"{self.numb}"  
    def __int__(self):
        return self.numb
    def __add__(self, other):
        numb1 = str(self.numb)
        try:
            numb2 = str(other.numb)
        except:
            numb2 = str(Maan(other).numb)
        ln1, ln2 = len(numb1), len(numb2)
        minLn = min(ln1,ln2)
        res = ""

        for i in range(1, minLn+1):
            res += str(max(int(numb1[-i]), int(numb2[-i])))

        prefixIndex = len(str(max(int(numb1), int(numb2))))-len(res)
        prefix = str(max(int(numb1), int(numb2)))[:prefixIndex]

        return Maan(int(prefix + res[::-1]))
    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        numb1 = str(self.numb)
        try:
            numb2 = str(other.numb)
        except:
            numb2 = str(Maan(other).numb)

        tempList = []
        for i, val in enumerate(int(max(int(numb1), int(numb2)))):
            pass

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, other):
        numb1 = str(self.numb)
        try:
            numb2 = str(other.numb)
        except:
            numb2 = str(Maan(other).numb)

        res = ""
        tempList = [int(i) for i in numb1]

        for i in range(len(tempList)):
            if tempList[i] != max(tempList):
                res += str(tempList[i])*min(int(numb1), int(numb2))
                continue
            res += str(tempList[i])
        return Maan(int(res))
    def __rpow__(self, other):
        return self.__pow__(other)

Maan(35) ** Maan(4)