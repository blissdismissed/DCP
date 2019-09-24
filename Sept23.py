# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

import sys
import math

def sumCheck(lst, num):
    #copy_lst = lst
    iter = 0
    for i in lst:
        #print(i)
        for j in lst:
            #print(j)
            #print("i: ",lst[int(i)])
            #print("j: ",lst[int(j)])
            #sum = int(i)+int(j)
            #print("Sum: ",sum)
            iter += 1
            if int(i)+int(j) == int(num):
                print("Iterations: ", iter)
                return True
    
    return False


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("You failed to enter enough arguments... Exiting.")
        sys.exit()

    lst = sys.argv[1].split(",")
    num = sys.argv[2]

    print("Problem 1: ")
    print("num: ", num)
    print("list: ", lst)
    print(sumCheck(lst,num))

    # What if either arg is missing? what if list is empty?
