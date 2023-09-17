#Geheimschrift

def codeer(lib, string):
    l = []
    for i in string:
        if i in [" ", ",", ".", "?", "!"] or i.isupper():
            l.append(i)
            continue
        l.append(lib[i.lower()])
    return "".join(l)

def decodeer(lib, string):
    lib = {v: k for k, v in lib.items()}
    l = []
    for i in string:
        if i in [" ", ",", ".", "?", "!"] or i.isupper():
            l.append(i)
            continue
        l.append(lib[i.lower()])
    return "".join(l)

codering = {chr(i):chr(i + 2) for i in range(ord('a'), ord('z'))}
codeer(codering, 'Dit is een gecodeerde tekst.')
decodeer(codering, 'Dkv ku ggp igeqfggtfg vgmuv.')

#Bewerking op Veeltermen

def parse_query(link, s = None):
    if s is None:
        s = {}
    loc_ind = link.index("?")
    s.update({"locatie": link[:loc_ind]})
    que_ind = link.index("#q=")+3
    s.update({"query": link[que_ind:].replace("+", " ")})
    r_args = (loc_ind+1, que_ind-3)
    l_args = link[r_args[0]:r_args[1]].split("&")
    args = {}
    for arg in l_args:
        ind = arg.index("=")
        args.update({arg[:ind]: arg[ind+1:]})
    s.update({"args": args})
    return s

parse_query('https://www.google.be/?gfe_rd=cr&ei=iMkkWKvMI9Dv8AfyrqDQBQ#q=tutorial+python')

#Omgekeerd Woordenboek - WIP

def inverteer(d, s = None):
    if s is None:
        s = {}
    for i in d:
        if d[i] not in s:
            s.update({d[i]: i})
        elif d[i] in s and isinstance(s[d[i]], list):
            s.update({d[i]: s[d[i]].append(i)})
        elif d[i] in s and s[d[i]] != list:
            s.update({d[i]: [s[d[i]], i]})
    return s

inverteer({i:i**2 for i in range(-5, 5)})

#Meervoudig Splitsen

def multi_split(x, sep, n = 0):
    p = []
    if n == len(sep):
        while "" in x:
            x.remove("")
        while "\n" in x:
            x.remove("\n")
        while "-" in x:
            x.remove("-")
        return x
    for i in enumerate(x):
        x[i[0]] = i[1].split(sep[n])
    for i in x:
        for j in i:
            
            p.append(j.lower())
    n += 1
    return multi_split(p, sep, n=n)

s = 'abc, def. ghi, jkl mno pqr, s'
t = 'ABC DEF, GHI'
multi_split([s, t],[',','.',' '])

#frequentietabel - Good enough

def frequentietabel(docu, l = None, d = None):
    open_docu = open(docu, "r")
    if l is None:
        l = []
    if d is None:
        d = {}
    for line in open_docu:
        l.append(line)
    l = multi_split(l, [".", ",", "?", " ", "\n", ":", "(", ")", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    l_set = set(l)
    for i in l_set:
        d.update({i: l.count(i)})
    return d

frequentietabel("dictionaries.txt")

#Compressie van Lijsten

def comprimeer(x, def_arg=None, d=None):
    if d is None:
        d = {}
    if def_arg is None:
        def_arg = [0,0]
    for i in set(x):
        if x.count(i) > def_arg[1]:
            def_arg[0] = i
            def_arg[1] = x.count(i)
    for i in enumerate(x):
        if i[1] == def_arg[0]:
            continue
        d.update({i[0]:i[1]})
    return (d, def_arg[0])

v = [0, 0, 0, 1, 1, 0, 0, 0, 2, 0, 0, 0, 3]
w = [1, 2, 0, 1, 2, 8, 1, 2, 7, 1, 2, 5, 1, 2]
x = [-3, -1, 5, -1, 2, 5, -1, 2, 7, -1, 2, 5, -1, 2]
comprimeer(x)

#Langste Cyclus

def max_cyclus(d, max=0, cur=0, n=None):
    for i in d:
        n = d[i]
        cur += 1
        while n != i:
            n = d[n]
            cur += 1
        if cur > max:
            max = cur
        cur = 0
    return max

v = {1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9, 7: 10, 8: 1, 9: 2, 10: 3}
w = {1: 5, 2: 1, 3: 2, 4: 3, 5: 6, 6: 10, 7: 7, 8: 8, 9: 9, 10: 4}
max_cyclus(w)