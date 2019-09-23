# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

import sys
import math


def sumCheck(lst, num):
    lst = [10,15,3,7]
    num = 17
    for i in lst:
        #print(i)
        for j in lst:
            #print(j)
            if i+j == num:
                return True
    return False


if __name__ == "__main__":

    lst = sys.argv[1]
    num = sys.argv[2]

    print("Problem 1: ")
    print(sumCheck(lst,num))
