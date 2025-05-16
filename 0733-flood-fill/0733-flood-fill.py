class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        original = image[sr][sc]
        
        if original == color:
            return image

        def DFS(i,j):
            if i<0 or j<0 or i>=n or j>=m:
                return
            if image[i][j] != original:
                return
            image[i][j]=color
            DFS(i+1,j)
            DFS(i-1,j)
            DFS(i,j+1)
            DFS(i,j-1)
            
        DFS(sr,sc)

        return image