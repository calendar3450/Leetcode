class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n= len(strs)
        result = []
        tmp = []
        

        for i in strs:
            sort_i = sorted(list(i))
            sort_j = ''
            for j in sort_i:
                sort_j +=j
            tmp.append(sort_j)

        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue

            tmp2 =[strs[i]]
            visited[i] = True

            for j in range(i+1,n):
                if not visited[j] and tmp[i] == tmp[j]:
                    tmp2.append(strs[j])
                    visited[j] = True

            result.append(tmp2)
        
        return result