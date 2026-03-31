from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = []

        for c in cnt:
            heapq.heappush(heap, (-cnt[c],c))

        result = []
        print(heap)
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result