import os
import sys

def surfaceArea(A):
    r = len(A)
    c = len(A[0])
    s = 0
    for i in range(0,r):
        for j in range(0,c):
            if(i==0):
                s += A[i][j]
            if(i==r-1):
                s += A[i][j]
            if(j==0):
                s += A[i][j]
            if(j==c-1):
                s += A[i][j]
            if(i==r-1 and j!=c-1):
                s += abs(A[i][j]-A[i][j+1])
            elif(i!=r-1 and j==c-1):
                s += abs(A[i][j]-A[i+1][j])
            elif(i==r-1 and j==c-1):
                pass
            else:
                s += abs(A[i][j]-A[i][j+1]) + abs(A[i][j]-A[i+1][j])
    s += 2*(r)*(c)
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    HW = input().split()
    H = int(HW[0])
    W = int(HW[1])
    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))
    result = surfaceArea(A)
    fptr.write(str(result) + '\n')
    fptr.close()
