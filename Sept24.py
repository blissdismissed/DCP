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
import time

def totalProductMethod(lst):
    #print("Method1: ")
    #print(lst)
    product = 1
    output = []

    if len(lst) < 2: return output
    for i in lst:
        product = i * product
    #print("Product = ",product)
    #print("Numpy product = ",numpy.product(lst))
    for i in lst:
        output.append(int(product / i))
    return output



def stepThroughArray(lst):
    #print("Method2: ")
    # initialize an array of same length as lst of all 1's
    outputLst = numpy.ones(len(lst), dtype = int)
    #print("Lst: ", lst)
    for i in range(len(lst)):
        #print("In lst: ", i, lst[i])
        for j in range(len(outputLst)):
            #print("In outputLst: ", j, outputLst[j])
            if i != j:
                outputLst[j] = outputLst[j] * lst[i]
    return outputLst


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You failed to enter a list... Exiting.")
        sys.exit()

    lst = sys.argv[1].split(",")
    lst = list(map(int, lst))

    start1 = time.time()
    method1Ans = totalProductMethod(lst)
    end1 = time.time()

    start2 = time.time()
    method2Ans = stepThroughArray(lst)
    end2 = time.time()

    print("Method 1 took: ",end1-start1)
    print("Method 2 took: ",end2-start2)

    print("Method1: ", method1Ans)
    print("Method2: ", method2Ans)
