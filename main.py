from back import *

d=pandas.read_csv('small-test-dataset.txt',sep=' ',header=None,engine='python',skipinitialspace=True)
curr = [3,5]
add = [7]
start = time.time()
print("Accuracy: "+str(validate(d,curr,add))) 
end = time.time()
print("Total time: "+str((end-start)*10**3)+" ms") 

d=pandas.read_csv('large-test-dataset-1.txt',sep=' ',header=None,engine='python',skipinitialspace=True)
curr = [1,15]
add = [27]
start = time.time()
print("Accuracy: "+str(validate(d,curr,add))) 
end = time.time()
print("Total time: "+str((end-start)*10**3)+" ms") 