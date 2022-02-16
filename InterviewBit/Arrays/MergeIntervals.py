# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        l = len(intervals)

        if l==0:
            return [new_interval]
        bi = 0
        if new_interval.start>intervals[-1].end : 
            return intervals+[new_interval]

        if new_interval.end<intervals[0].start :
            return [new_interval]+intervals
        
        st_index = -1
        ei_index = -1
        for ind, i in enumerate(intervals) :
            if new_interval.start >= i.start and new_interval.end <= i.end :
                return intervals
            if st_index == -1 and new_interval.start <= i.end : 
                st_index = ind
            if new_interval.end >= i.start : 
                ei_index = ind
        
        res = []
        for i in range(st_index) :
            res.append(intervals[i])
        res.append(Interval(min(new_interval.start, intervals[st_index].start), max(new_interval.end, intervals[ei_index].end)))
        for i in range(ei_index+1, l):
            res.append(intervals[i])
    
        return res
