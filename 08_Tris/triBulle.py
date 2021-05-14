# Tri Bulle

def triBulle(l):
    for i in range(len(l)-1,0,-1):
        for j in range(0,i):
            if l[j+1]<l[j]:
                l[j+1],l[j]=l[j],l[j+1]
    return l


def triBulleOpti(l):
    for i in range(len(l)-1,0,-1):
        tableauTriee,j = True,0
        while tableauTriee and j<i:
            if l[j+1]<l[j]:
                l[j+1],l[j]=l[j],l[j+1]
                tableauTriee= False
            j+=1
    return l

l=[10,3,6,2,9,3,1]

triBulle(l)
triBulleOpti(l)