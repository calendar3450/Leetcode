from collections import Counter,deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)

        heaps = [-c for c in cnt.values()]
        heapq.heapify(heaps)
        cool = deque()
        time = 0

        while heaps or cool:
            time +=1
            
            if heaps:
                c= heapq.heappop(heaps)
                c+=1
                if c != 0:
                    cool.append((time + n, c))

            if cool and cool[0][0] == time:
                a, c = cool.popleft()
                heapq.heappush(heaps, c)

        return time

        