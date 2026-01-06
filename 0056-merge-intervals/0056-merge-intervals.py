class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        tmp = intervals[0]

        for interval in intervals:
            if tmp[0] <= interval[0] and tmp[1] >= interval[0] and tmp[1] <= interval[1]:
                tmp[1] = interval[1]
            
            if tmp[1] < interval[0]:
                ans.append(tmp)
                tmp = interval

        ans.append(tmp)
        
        return ans