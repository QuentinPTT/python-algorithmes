# Méthode de la fausse position

def f(x):
    return -1/2*x**2+5*x-5

def faussePos (f,a,b,eps):
    g,d=a,b
    status = False
    while not status:
        m = (g * f(d) - d*f(g))/(f(d)-f(g))
        if f(m) * f(g) <= 0:
            d = m
        else:
            g = m
        if f(m) * f(m - eps) <= 0 or f(m) * f(m - eps) <= 0:
            status = True
    return m

faussePos(f, 0 , 2, 10**(-5))