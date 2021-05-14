# Calcul la variance d'une liste

def varianceListe(l):
    variance = 0
    moy = moyenneListe(l)
    for k in range(len(l)):
        variance+=(l[k] - moy)**2
    return variance/len(l)

def varianceListe2(l):
    variance = 0
    moy = moyenneListe(l)
    for k in range(len(l)):
        variance+= l[k]**2
    return variance/len(l) - moy**2

l=[3,2,5,1,6,1]

varianceListe(l)
varianceListe2(l)