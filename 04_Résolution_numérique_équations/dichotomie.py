# Méthode de la dichotomie

def dichotomie1(f,a,b,n):
    g=a
    d=b
    for k in range (1,n+1):
        m=(g+d)/2
        if f(d)*f(m)>0:
            d=m
        else:
            g=m
    return m

def dichotomie2(f,a,b,eps):
    g=a
    d=b
    while abs(g-d)>eps:
        m=(g+d)/2
        if f(d)*f(m)>0:
            d=m
        else:
            g=m
    return m

dichotomie1(f,0,3,10)
dichotomie2(f,0,3,10**(-3))