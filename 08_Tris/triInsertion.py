# Tri par insertion

def triInsertion(l):
    for i in range(1, len(l)):
        x,j=l[i],i
        while j>0 and l[j-1]>x:
            l[j]=l[j-1]
            j-=1
        l[j]=x
    return l

l=[10,3,6,2,9,3,1]

triInsertion(l)