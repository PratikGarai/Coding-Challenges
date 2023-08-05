class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        s = {}
        l = len(nums)
        for i in nums : 
            if i in s : 
                s[i] += 1
            else : 
                s[i] = 1
        
        c = []
        for i in s : 
            if s[i] > l/3 : 
                c.append(i)
        
        return c
