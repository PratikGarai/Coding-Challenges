class Solution:
    
    def doOverlap(self, l1, r1, l2, r2):
        #code here
        
        if (l1[0] > r2[0] or l2[0] > r1[0]) :
            return 0;
           
        if (r1[1] > l2[1] or r2[1] > l1[1]) :
            return 0;

        return 1;
