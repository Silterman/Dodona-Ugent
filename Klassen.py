#Harmonische Trilling

import math

class HarmonischeTrilling:
    def __init__(self, A, w, o):
        self.A = A
        self.w = w
        self.o = o
    def value(self, t):
        return self.A*math.cos(self.w*t + self.o)

a = HarmonischeTrilling(2.5, 1.0, math.pi/2)
a.value(1.0)

#Boeken in een Bibliotheek

class Boek:
    def __init__(self, titel, nummer, auteur, anlt_ontleend = 0):
        self.titel =  titel
        self.nummer = nummer
        self.auteur = auteur
        self.ontleend = False
        self.antl_ontleend = anlt_ontleend
    def get_titel(self):
        return self.titel
    def get_catalogusnummer(self):
        return self.nummer
    def get_auteur(self):
        return self.auteur
    def is_uitgeleend(self):
        return self.ontleend
    def get_aantal_ontleningen(self):
        return self.antl_ontleend
    def set_titel(self, titel):
        self.titel = titel
    def set_catalogusnummer(self, nummer):
        self.nummer = nummer
    def set_auteur(self, auteur):
        self.auteur = auteur
    def ontleen(self):
        if self.ontleend == False:
            self.ontleend = True
            self.antl_ontleend += 1
            return True
        else:
            return False
    def breng_terug(self):
        if self.ontleend == True:
            self.ontleend = False
            return True
        else:
            return False

#Vakscores

class Vakscore:
    def __init__(self, naam, maxScore = 20):
        self.naam = naam
        self.maxScore = maxScore
        self.scores = []
    def get_naam(self):
        return self.naam
    def voeg_toe(self, score):
        if 0 <= score <= self.maxScore:
            self.scores.append(score)
            return True
        else:
            return False
    def gemiddelde(self):
        return sum(self.scores)/len(self.scores)
    def aantal_ABC(self):
        return [sum(map(lambda x: x >= 0.6*self.maxScore, self.scores)),sum(map(lambda x: 0.6*self.maxScore > x >= 0.5*self.maxScore, self.scores)),sum(map(lambda x: x<0.5*self.maxScore, self.scores))]

#IPv4 Adressen

class InternetAdres:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def get_adres(self):
        return [self.a, self.b, self.c, self.d]
    def get_klasse(self):
        if self.a <= 127:
            return "A"
        elif self.a <= 191:
            return "B"
        elif self.a <= 223:
            return "C"
        elif self.a <= 240:
            return "D"
        return "E"