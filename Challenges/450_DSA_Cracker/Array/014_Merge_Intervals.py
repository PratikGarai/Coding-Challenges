class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        start = intervals[0][0]
        end = intervals[0][1]

        res = []

        for point in intervals : 
            if start <= point[0] and end >= point[1] : 
                continue
            elif start <= point[0] and end >= point[0] : 
                end = point[1]
            else : 
                res.append([start, end])
                start = point[0]
                end = point[1]
        
        res.append([start, end])
        return res
