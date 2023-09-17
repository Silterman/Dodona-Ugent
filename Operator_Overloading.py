#lineaire benadering

class LineaireBenadering:
    def __init__(self, f, a, h=1E-10):
        self.f = f
        self.a = a
        self.h = h
    def __call__(self, x):
        return self.f(self.a) + ((self.f(self.a+self.h)-self.f(self.a))/self.h)*(x-self.a)

#Kassa

class Kassa:
    def __init__(self, naam):
        self.naam = naam
        self.kassa_stand = 0
        self.pos_trans = 0
        self.neg_trans = 0
    def __str__(self):
        return "[%s:%f]"%(self.naam, self.kassa_stand)
    def __repr__(self):
        return 'Kassa("%s")'%(self.naam)
    def get_positieve_transacties(self):
        return self.pos_trans
    def get_negatieve_transacties(self):
        return self.neg_trans
    def __eq__(self, value):
        return self.naam == value
    def __iadd__(self, value):
        if (self.kassa_stand + value) < 0:
            return self
        self.kassa_stand += value
        if value < 0:
            self.neg_trans += 1
            return self
        self.pos_trans += 1
        return self
    def __isub__(self, value):
        if self.kassa_stand - value < 0:
            return self
        self.kassa_stand -= value
        if value < 0:
            self.pos_trans += 1
            return self
        self.neg_trans += 1
        return self

#Studenten en Punten

class Student:
    def __init__(self, naam, vakken=None, antl_vakken=0):
        self.naam = naam
        if vakken is None:
            vakken = {}
        self.vakken = vakken
        self.antl_vakken = max(sum(self.vakken), antl_vakken)
    def __str__(self):
        return "[%s:%d]"%(self.naam, self.antl_vakken)
    def __repr__(self):
        return "Student('%s')"%self.naam
    def __eq__(self, value):
        return self.naam == value.naam
    def __ne__(self, value):
        return self.naam != value.naam
    def __iadd__(self, value):
        self.vakken.update({value[0]:value[1]})
        self.antl_vakken = len(self.vakken)
        return self
    def __call__(self, vak=None):
        if vak == None:
            return self.naam
        else:
            return self.vakken[vak]
        

s1 = Student('Jan Jansens')
s2 = Student('Jan Klaassen')
s3 = Student('Jan Jansens')
print(s1 == s3)