 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    def findLongestConseqSubseq(self,arr, N):
        s = set()
        for i in arr : 
            s.add(i)
        
        ml = 0
        for i in s : 
            if i-1 in s : 
                continue
            else :
                c = 0
                ele = i
                while ele in s : 
                    c += 1
                    ele += 1
                ml = max(c, ml)
        return ml


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends
