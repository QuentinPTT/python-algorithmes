# PGCD

def pgcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

pgcd(27,18)