#Given an array of integers, return a new array such that each 
# element at index i of the new array is the product of all the 
# numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected 
# output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
# the expected output would be [2, 3, 6].
#
#Follow-up: what if you can't use division?


# Method 1: With Division

import math
import sys

def totalProductMethod():
    print("Method1: ")

def stepThroughArray():
    print("Method2: ")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("You failed to enter enough arguments... Exiting.")
        sys.exit()

    lst = sys.argv[1].split(",")
    num = sys.argv[2]

    print("Problem 2: ")
    totalProductMethod()
    stepThroughArray()
    #print("num: ", num)
    #print("list: ", lst)
    #print(sumCheck(lst,num))