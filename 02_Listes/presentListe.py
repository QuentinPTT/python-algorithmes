# Présence d'un élément dans une liste

def presentListe(l,x):
    present = False
    for k in range(len(l)):
        if l[k] == x:
            present = True
    return present

def presentListe2(l,x):
    present,k = False,0
    while k<len(l) and not present:
        if l[k] == x:
            present = True
        k+=1
    return present

l=[3,2,5,1,6,1]

presentListe(l,1)
presentListe2(l,1)