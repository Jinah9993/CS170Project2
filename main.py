from featureSearch import *

r = True
while r:
    print("Welcome to the Feature Selection Algorithm.")
    file_name = input("Enter the name of the file to test: \n")
    d = pandas.read_csv(file_name, sep=' ', header = None, engine = 'python', skipinitialspace = True)
    #small-test-dataset.txt
    #large-test-dataset-1.txt
    #CS170_Spring_2023_Large_data__35.txt 
    #CS170_Spring_2023_Small_data__35.txt
    print("Type the number of the algorithm you want to run.\n")
    print("\t1)  Forward Selection")
    print("\t2)  Backward Elimination")
    print("\t3)  Our Special Algorithm :)")
    alg_choice = int(input())
    bestFeatures = []

    if alg_choice == 1:
        bestFeatures = forward(d)
    elif alg_choice == 2:
        bestFeatures = back(d)
    elif alg_choice == 3:
        print("Hello World!")
    else:
        print("Your Input is Wrong")
        print("Please make a Selection from 1 to 3")



    print("---------------------------------")
    print("Accuracy: " + str(bestFeatures[1]))
    print("Best Features: ")
    print(bestFeatures[0]) 
    print("---------------------------------")
    
    r = False

 

