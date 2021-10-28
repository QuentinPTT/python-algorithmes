# Nombres occurences

def nombresOccurences(l,x):
    occurences = 0
    for k in range(len(l)):
        if l[k] == x:
            occurences+=1
    return occurences

l=[3,2,5,1,6,1]

nombresOccurences(l,1)