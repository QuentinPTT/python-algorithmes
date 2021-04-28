from math import *
def f(x):
    return cos(x)-x

def fp(x):
    return -sin(x)-1

# Méthode de Newton

def newton1(f,fp,u0,n):
    u=u0
    for k in range (1,n+1):
        u-=f(u)/fp(u)
    return u

def newton2(f,fp,u0,eps):
    un=u0
    un1=un-f(un)/fp(un)
    while abs(un1-un)>eps:
        un=un1
        un1=un-f(un)/fp(un)
    return un

def newton3(f,fp,u0,eps):
    u=u0
    while f(u-eps)*f(u+eps)>0:
        u-=f(u)/fp(u)
    return u

newton1(f,fp,0,10)
newton2(f,fp,0,10**(-2))
newton3(f,fp,0,10**(-2))