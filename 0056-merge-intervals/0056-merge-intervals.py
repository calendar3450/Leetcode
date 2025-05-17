class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        tmp = intervals[0]

        for i in range(1,len(intervals)):
            if intervals[i][0] > tmp[1]:
                result.append(tmp)
                tmp = intervals[i]
            else:
                if tmp[1]< intervals[i][1]:
                    tmp[1]= intervals[i][1]
                
        result.append(tmp)

        return result

                
            