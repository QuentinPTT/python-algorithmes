# PGCD

def pgcd(a,b):
    if b > 0: 
        return pgcd(b,a%b)
    else: 
        return a
    
pgcd(27,18)