# Méthode des trapèzes

def trapeze(f,a,b,n):
    s=0
    h=(b-a)/n
    for k in range (1,n):
        s+= h*f(a+k*h)
    s+= h*(f(a)+f(b))/2
    return s

trapeze(cos,0,pi/2,10)