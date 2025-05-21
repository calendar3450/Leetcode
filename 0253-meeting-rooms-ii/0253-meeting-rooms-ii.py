import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        meetingroom = []
        heapq.heappush(meetingroom,intervals[0][1])

        for i in range(1,len(intervals)):
            if intervals[i][0]>=meetingroom[0]:
                heapq.heappop(meetingroom)
            
            heapq.heappush(meetingroom,intervals[i][1])

        return len(meetingroom)