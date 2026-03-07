import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        heap = []
        max_val = float('-inf')

        for i in range(len(nums)):
            val = nums[i][0]
            heap.append((val,i,0))
            max_val = max(max_val,val)

        best_range = [float('-inf'), float('inf')]
        heapq.heapify(heap)
        print(heap)
        
        while True:
            min_val, row,col = heapq.heappop(heap)

            if max_val - min_val < best_range[1] - best_range[0]:
                best_range = [min_val,max_val]

            if col + 1 == len(nums[row]):
                break
            
            next_val = nums[row][col +1]
            heapq.heappush(heap, (next_val, row, col + 1))

            max_val = max(max_val,next_val)

        return best_range