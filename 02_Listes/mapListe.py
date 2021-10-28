# Map d'une liste

def f(x):
    return x**2

def mapListe(l,f):
    for k in range(len(l)):
        l[k] = f(l[k])
    return l

l=[x for x in range(5)]

mapListe(l,f)