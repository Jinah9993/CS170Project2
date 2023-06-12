from back import *

def print_result(d, curr, add):
    start = time.time()
    accuracy = validate(d, curr, add)
    end = time.time()
    total_time = (end - start) *10**3
    print("---------------------------------")
    print("Accuracy: " + str(accuracy))
    print("Total time: "+ str((total_time))+" ms") 
    print("---------------------------------")


def main():
    while True:
        print("Welcome to XXX Feature Selection Algorithm.")
        file_name = input("Enter the name of the file to test: \n") 
        ##small-test-dataset.txt
        ##large-test-dataset-1.txt
        ##CS170_Spring_2023_Large_data__35.txt 
        ##CS170_Spring_2023_Small_data__35.txt
        print("Type the number of the algorithm you want to run.\n")
        print("\t1)  Forward Selection")
        print("\t2)  Backward Elimination")
        print("\t3)  Our Special Algorithm :)")
        alg_choice = int(input())

        if alg_choice == 1:
            d=pandas.read_csv(file_name,sep=' ',header=None,engine='python',skipinitialspace=True)
            curr = []
            add = []
            print_result(d,curr,add)
        elif alg_choice == 2:
            d=pandas.read_csv(file_name,sep=' ',header=None,engine='python',skipinitialspace=True)
            curr = []
            add = []
            print_result(d,curr,add)
        elif alg_choice == 3:
            print("Hello World!")
        else:
            print("Your Input is Wrong")
            print("Please make a Selection from 1 to 3")

main()
            
'''

d=pandas.read_csv('small-test-dataset.txt',sep=' ',header=None,engine='python',skipinitialspace=True)
curr = [3,5]
add = [7]
print_result(d,curr,add)

d=pandas.read_csv('large-test-dataset-1.txt',sep=' ',header=None,engine='python',skipinitialspace=True)
curr = [1,15]
add = [27]
print_result(d,curr,add)
'''