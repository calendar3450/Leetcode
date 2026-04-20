from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[a].append(b)

        state = [0] * numCourses

        def DFS(node):
            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            state[node] = 1

            for nxt in graph[node]:
                if not DFS(nxt):
                    return False
            state[node] = 2
            return True

        for i in range(numCourses):
            if not DFS(i):
                return False
        
        return True

        



        
        