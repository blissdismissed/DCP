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
import numpy

def totalProductMethod(lst):
    #print("Method1: ")
    #print(lst)
    product = 1
    output = []

    if len(lst) < 2: return output
    for i in lst:
        product = i * product
    print("Product = ",product)
    print("Numpy product = ",numpy.product(lst))
    for i in lst:
        output.append(int(product / i))
    return output



def stepThroughArray(list):
    #print("Method2: ")
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You failed to enter a list... Exiting.")
        sys.exit()

    lst = sys.argv[1].split(",")
    lst = list(map(int, lst))

    print("Problem 2: ")
    method1Ans = totalProductMethod(lst)
    method2Ans = stepThroughArray(lst)

    print("Method1: ", method1Ans)
    #print("list: ", lst)
    #print(sumCheck(lst,num))