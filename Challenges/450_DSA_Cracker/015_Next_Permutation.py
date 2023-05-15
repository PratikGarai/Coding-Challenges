class Solution:
    def reverse(self, nums, begin, end) :
        for i in range((end-begin)//2) :
            nums[begin+i], nums[end-1-i] = nums[end-1-i], nums[begin+i] 

    def nextPermutation(self, nums: List[int]) -> None:
        l = len(nums)
        if l == 1 : 
            return
        
        ind = l-2
        while ind >= 0 and nums[ind] >= nums[ind+1] : 
            ind -= 1
        
        if ind == -1 : 
            self.reverse(nums, 0, l)
        else : 
            ele = nums[ind]
            tind = ind
            self.reverse(nums, ind+1, l)
            ind += 1
            while ind < l and nums[ind] <= ele : 
                ind += 1
            nums[tind], nums[ind] = nums[ind], nums[tind]
            
