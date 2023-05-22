from back import *


d = [0,1,2,3,4]
print("--Testing forward selection--")
best = forward(d)
print("--Forward selection results--")
print("Best features: ")
print(best[0])
print("Best score: ")
print(best[1])

print("--Testing backward elimination--")
best = back(d)
print("--Backward elimination results--")
print("Best features: ")
print(best[0])
print("Best score: ")
print(best[1])