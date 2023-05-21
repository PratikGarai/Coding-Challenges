from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :
    c0, c1, c2 = 0, 0, 0
    for i in arr : 
        if i == 0 : 
            c0 += 1
        elif i ==1 : 
            c1 += 1
        else : 
            c2 += 1
    for i in range(c0) :
        arr[i] = 0
    for i in range(c0, c0+c1) :
        arr[i] = 1
    for i in range(c0+c1, n) : 
        arr[i] = 2


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())
	if n == 0 :
		return list(), 0
	arr = list(map(int, stdin.readline().strip().split(" ")))
	return arr, n


def printAnswer(arr, n) :
    for i in range(n) :
        print(arr[i],end=" ")
    print()
    
#main
t = int(input().strip())
for i in range(t) :
    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
