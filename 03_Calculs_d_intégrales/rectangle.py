# Méthode des rectangles

def rectangle(f,a,b,n):
    h=(b-a)/n
    s=0
    for k in range (0,n):
        s+=h*f(a+k*h)
    return s

rectangle(cos,0,pi/2,10)