# Méthode de la corde

def f(x):
    return -1/2*x**2+5*x-5

def corde(f,a,b,eps):
    x,y,n = a,b,0
    while abs(x-y) > eps and n<50:
        n+=1
        z = (x*f(y) - y*f(x))/(f(y)-f(x))
        x,y = y,z
    if n < 50:
        return y
    else:
        print("Aucune solution n'a été trouvée'")

corde(f,0,2,10**(-5))