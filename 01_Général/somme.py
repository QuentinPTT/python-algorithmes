# Technique pour la somme

def f(k):
    return 1/k**2

def somme(n,f):
    somme = 0
    for k in range(1,n+1):
        somme += f(k)
    return somme

somme(100,f)