import numpy
import pandas
import math
import time
def validate(d,curr,add): 
    c = 0
    classes=d.iloc[:,c].values
    f=d.iloc[:,curr+add].values
    for i in range(len(d)):
        dist = math.inf
        neighbor = 111
        nClass = 111
        print("Object "+str(i+1)+" is of class "+str(int(classes[i])))
        start = time.time()
        for j in range(len(d)):
            if i != j:
                currDist=math.sqrt(sum(pow((f[i]-f[j]),2)))
                if currDist<dist:
                    dist = currDist
                    neighbor = j
                    nClass = classes[j]
        end = time.time()
        print("Its nearest neighbor is Object "+str(neighbor+1)+" of class "+str(int(nClass)))
        print("Time taken: "+str((end-start)*10**3)+" ms")
        if classes[i]==nClass:
            c=c+1
    return c/len(d)

