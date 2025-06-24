class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        result = []

        for i,j in enumerate(points):
            distance.append([j[0]**2 + j[1]**2,i])
        
        distance.sort()
        for i in range(k):
            result.append(points[distance[i][1]])

        return result
        
