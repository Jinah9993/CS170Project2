import random as r
from classify import *


def default(d):
    l = d.iloc[:,0]
    c = l.value_counts() 
    c = c.tolist() 
    s = c[0] / d.shape[0]
    return s


def forward(d):
    f =d.shape[1] -1
    f = range(f)
    f = numpy.array(f) + 1
    f = list(f)
    used = []
    best = []
    score = default(d)
    for i in range(len(f)):
        print("Level "+str(i+1)+" of the search tree.")
        add = 0
        currBest = 0 
        for j in range(len(f)):
            if f[j] not in used: 
                dummy = []
                dummy.append(f[j]) 
                a = validate(d,used,dummy)
                print("--Considering adding feature "+str(f[j])+". Score = "+str(a))
                if a >currBest:
                    currBest = a
                    add = f[j]
        used.append(add)
        print("Level "+str(i+1)+": added feature " +str(add))
        if currBest > score:
            score = currBest
            best = []
            for i in range(len(f)):
                if f[i] in used:
                    best.append(f[i])
    return [best,score]



def back(d):
    f =d.shape[1] -1
    f = range(f)
    f = numpy.array(f) + 1
    f = list(f)
    remove = []
    best = []
    score = default(d)
    
    
    for i in range(len(f)):
        print("Level "+str(i+1) +" of the search tree.")
        removed = 0
        currBest = 0 
        for j in range(len(f)):
            if f[j] not in remove:   
                dummy = []
                dummy.append(f[j]) 
                a =validate(d,remove,dummy)
                print("--Considering removing feature "+str(f[j])+ ". Score = " + str(a))
                if a >currBest:
                    currBest = a
                    removed = f[j]
        remove.append(removed)
        print("Level "+str(i+1)+": removed feature " + str(removed))
        if currBest > score:
            score = currBest
            best = []
            for i in range(len(f)):
                if f[i] in remove:
                    best.append(f[i])
    return [best,score]