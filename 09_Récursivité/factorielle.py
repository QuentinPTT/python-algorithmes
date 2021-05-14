# Calcul de factorielle

def factorielle(x):
    if x>0:
        return x*factorielle(x-1)
    else: 
        return 1
    
factorielle(10)