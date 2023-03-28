from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    beg = m+1
    end = len(arr)-1
    mid = (end + beg) // 2
    for i in range(beg, mid+1) :
        arr[i], arr[end-(i-beg)] = arr[end-(i-beg)], arr[i]
    return arr
