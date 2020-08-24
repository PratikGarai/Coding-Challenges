#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr = sorted(arr)
    l = len(arr)
    if k>l:
        k = l
    if k==l:
        return arr[l-1]-arr[0]
    m = arr[l-1]-arr[0]
    if m==0:
         return 0
    for i in range(0, l-k+1):
        if (arr[i+k-1]-arr[i])<m:
            m = arr[i+k-1]-arr[i]
    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
