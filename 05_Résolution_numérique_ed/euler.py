# Méthode d'Euler

def euler(f,a,b,y0,n):
    h=(b-a)/n
    yk=y0
    tk=a
    L=[y0]
    for k in range(1,n+1):
        yk+=h*f(tk,yk)
        tk+=h
        L.append(yk)
    return L