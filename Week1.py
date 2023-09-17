#ISBN

x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
x6 = int(input())
x7 = int(input())
x8 = int(input())
x9 = int(input())

x10 = (x1 + 2*x2 + 3*x3 + 4*x4 + 5*x5 + 6*x6 + 7*x7 + 8*x8 + 9*x9)%11
print(x10)

#SomVanTweeGetallen

n, m = int(input()), int(input())
print(n+m)

#WaarIsDeVader

a, b, c = int(input()), int(input()), int(input()) #jaren ouder/jaren nodig voor veelvoud te bekomen/veelvoud

x0 = (a+b)/c - b
x1 = c/(c-1)

z = round(x0*x1*12) #leeftijd zoon
m = z+a*12 #leeftijd moeder

s = "De moeder is %s maanden oud en haar zoon %s maanden."
print(s % (str(m),str(z)))

#ISBN

x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
x6 = int(input())
x7 = int(input())
x8 = int(input())
x9 = int(input())
x10 = int(input())

if x10 == (x1 + 2*x2 + 3*x3 + 4*x4 + 5*x5 + 6*x6 + 7*x7 + 8*x8 + 9*x9)%11:
    print("OK")
else:
    print("FOUT")

#Hertzsprung-Russelldiagram

T, Lc = float(input()), float(input())

if Lc >= 10000:
    print("superreuzen (a)")
elif 10000 > Lc >= 1000:
    print("superreuzen (b)")
elif 1000 > Lc >= 100 and T < 7500:
    print("heldere reuzen")
elif 100 > Lc >= 10 and T < 6000:
    print("reuzen")
elif (Lc <= 0.01 and  T >= 5000) or (Lc <= 0.0001 and  T >= 3000):
    print("witte dwergen")
else:
    print("hoofdreeks")

#vierkaartenprobleem

side = str(input())
if side == "waarde":
    waarde = int(input())
    draaien = str(input())

    if waarde%2 == 0 and draaien == "ja":
        print("Juist: kaarten met waarde %d moeten gedraaid worden." % waarde)
    elif waarde%2 != 0 and draaien == "ja":
        print("Fout: kaarten met waarde %d moeten niet gedraaid worden." % waarde)
    elif waarde%2 != 0 and draaien == "nee":
        print("Juist: kaarten met waarde %d moeten niet gedraaid worden." % waarde)
    elif waarde%2 == 0 and draaien == "nee":
        print("Fout: kaarten met waarde %d moeten gedraaid worden." % waarde)
elif side == "kleur":
    waarde = str(input())
    draaien = str(input())

    if waarde != "rood" and draaien == "ja":
        print("Juist: kaarten met kleur %s moeten gedraaid worden." % waarde)
    elif waarde == "rood" and draaien == "ja":
        print("Fout: kaarten met kleur %s moeten niet gedraaid worden." % waarde)
    elif waarde == "rood" and draaien == "nee":
        print("Juist: kaarten met kleur %s moeten niet gedraaid worden." % waarde)
    elif waarde != "rood" and draaien == "nee":
        print("Fout: kaarten met kleur %s moeten gedraaid worden." % waarde)

#ISBN

x1 = input()
while x1 != "stop":
    x1 = int(x1)
    x2 = int(input())
    x3 = int(input())
    x4 = int(input())
    x5 = int(input())
    x6 = int(input())
    x7 = int(input())
    x8 = int(input())
    x9 = int(input())
    x10 = int(input())

    if x10 == (x1 + 2*x2 + 3*x3 + 4*x4 + 5*x5 + 6*x6 + 7*x7 + 8*x8 + 9*x9)%11:
        print("OK")
    else:
        print("FOUT")

    x1 = input()

#canvascrack

n = int(input()) #aantal tafels crack
e = int(input()) #waarde per tafel
w = int(input()) #aantal gewonnen tafels per verdubbeling
s = str(input()) #status van de crack (verloren of gestopt)

pot = 0

for i in range(1,n):
    if i%w == 0:
        pot = int((pot+i*e)*2)
        print("tafel #%d (x2): €"%i + str(pot))
    else:
        pot += i*e
        print("tafel #%d: €"%i + str(pot))

if s == "gestopt":
    if n%w == 0:
        pot = (pot+n*e)*2
        print("tafel #%d (x2): €"%n + str(pot))
    else:
        pot += n*e
        print("tafel #%d: €"%n + str(pot))

if s == "verloren":
    pot = int(pot/2)
    print("tafel #%d: €"%n + str(pot))



#biljarttafel - does not work

y_max = int(input())
x_max = int(input())

p = [(0,0),(0,y_max),(x_max,0),(x_max,y_max)]

m = [(1,1), (1, -1), (-1,-1), (-1, 1)]
n = 0

x = 1
y = 1

while (x,y) not in p:
    if x in [0, x_max]:
        if x == 0:
            print("linkerband " + str((x, y)))
        elif x == x_max:
            print("rechterband " + str((x, y)))
        n = (n + 1)%4
    elif y in [0, y_max]:
        if y  == 0:
            print("onderband " + str((x, y)))
        elif y == y_max:
            print("bovenband " + str((x, y)))
        n = (n + 1)%4
    x += m[n][0]
    y += m[n][1]

if x == 0:
    if y == 0:
        print("linkeronderpocket " + str((x,y)))
    elif y == y_max:
        print("linkerbovenpocket " + str((x,y)))
if x == 8:
    if y == 0:
        print("rechteronderpocket " + str((x,y)))
    elif y == y_max:
        print("rechterbovenpocket " + str((x,y)))


#De drie wijzen

t = float(input())

f"€{0} + €{0} + €{0} = €{0} x €{0} x €{0} = €{t}"