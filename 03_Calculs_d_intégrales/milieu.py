# Méthode des milieux

def milieu(f,a,b,n):
    s=0
    h=(b-a)/n
    for k in range(0,n):
        s+=h*f(a+k*h+h/2)
    return s

milieu(cos,0,pi/2,10)