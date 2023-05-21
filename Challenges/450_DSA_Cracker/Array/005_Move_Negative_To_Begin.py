from os import *
from sys import *
from collections import *
from math import *

def separateNegativeAndPositive(nums):
    
    n = 0
    l = len(nums)
    for i in range(l):
        if nums[i] < 0 : 
            nums[i], nums[n] = nums[n], nums[i]
            n += 1 

    return nums
