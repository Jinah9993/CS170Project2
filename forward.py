from func import *
def forward(d):
    f =d[1:]
    used = []
    best = []
    score = default(f)
    for i in range(len(f)):
        print("Level "+str(i+1)+" of the search tree.")
        add = 0
        currBest = 0 
        for j in range(len(f)):
            if f[j] not in used:    
                a = eval(f,used,f[j])
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