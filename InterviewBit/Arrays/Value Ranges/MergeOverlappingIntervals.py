# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):

        l = len(intervals)
        if l==0 or l==1:
            return intervals
        intervals = sorted(intervals, key = lambda x : x.start)
        res = []
        last_interval = Interval(intervals[0].start, intervals[0].end)
        for i in intervals[1:] :
            if last_interval.end >= i.start : 
                last_interval.end = max(last_interval.end, i.end)
            else :
                res.append(last_interval)
                last_interval = i
        
        res.append(last_interval)
        
        return res
