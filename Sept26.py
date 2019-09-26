# Sept 26
# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

import math
import sys

def findInt(inputs):
    i = 1
    while i <= len(inputs):
        if i in inputs: i += 1
        else: return i


if __name__ == '__main__':
    input1 = [3,4,-1,1] # => 2
    input2 = [1,2,0] # => 3
    print("Input 1: ",findInt(input1))
    print("Input 2: ",findInt(input2))

