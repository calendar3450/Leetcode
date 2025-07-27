from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxf = max(freq.values())
        count = sum(1 for v in freq.values() if v == maxf)

        part_count = maxf - 1
        part_length = n + 1
        min_slots = part_count * part_length + count

        return max(len(tasks), min_slots)
 

            
        
        
        
