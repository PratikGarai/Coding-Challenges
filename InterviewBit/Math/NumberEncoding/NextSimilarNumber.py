class Solution:
    # @param A : string
    # @return a strings

    def solve(self, A):

        nums = [int(i) for i in A]

        def ints_to_str(ints) : 
            s = ""
            for i in ints :
                s += str(i)
            return s

        l = len(nums)
        for i in range(len(nums)-2, -1, -1) :
            if nums[i+1]>nums[i]:
                buf = sorted(nums[i:])
                le = len(buf)
                for j in range(1, le) :
                    if buf[j-1]==nums[i] and buf[j]!=buf[j-1] :
                        return ints_to_str(nums[:i])+str(buf[j])+ints_to_str(buf[:j])+ints_to_str(buf[j+1:])

        return "-1"
