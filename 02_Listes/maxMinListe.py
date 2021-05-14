# Maximum et Minimum d'une liste

def maxListe(l):
    x = l[0]
    for k in range(1,len(l)):
        if l[k]>x:
            x=l[k]
    return x

def minListe(l):
    x = l[0]
    for k in range(1,len(l)):
        if l[k]<x:
            x=l[k]
    return x

l=[10,3,6,27,9,3,1]

maxListe(l)
minListe(l)