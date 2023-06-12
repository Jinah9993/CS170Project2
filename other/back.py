from forward import *
def back(d):
    f =d.shape[1] -1
    f = range(f)
    
    remove = []
    best = []
    score = default(f)
    
    for i in range(len(f)):
        print("Level "+str(i+1) +" of the search tree.")
        removed = 0
        currBest = 0 
        for j in range(len(f)):
            if f[j] not in remove:    
                a =validate(f,remove,f[j])
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
                if f[i] not in remove:
                    best.append(f[i])
    return [best,score]