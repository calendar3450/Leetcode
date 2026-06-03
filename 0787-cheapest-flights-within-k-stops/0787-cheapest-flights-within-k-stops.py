from collections import deque, defaultdict
import sys

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # 1. 그래프 빌드 (adj list)
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
            
        # 각 도시별 최소 비용 초기화
        min_prices = [sys.maxsize] * n
        min_prices[src] = 0
        
        # 큐 초기화: (현재 도시, 현재 누적 비용)
        queue = deque([(src, 0)])
        stops = 0
        
        # 최대 k번 경유 = 최대 k+1번 이동
        while queue and stops <= k:
            # 현재 레벨(이동 횟수)의 노드 수만큼만 순회
            for _ in range(len(queue)):
                curr_node, curr_price = queue.popleft()
                
                for neighbor, price in graph[curr_node]:
                    next_price = curr_price + price
                    
                    # 더 저렴한 경로를 찾은 경우에만 갱신하고 큐에 삽입
                    if next_price < min_prices[neighbor]:
                        min_prices[neighbor] = next_price
                        queue.append((neighbor, next_price))
            stops += 1
            
        return min_prices[dst] if min_prices[dst] != sys.maxsize else -1