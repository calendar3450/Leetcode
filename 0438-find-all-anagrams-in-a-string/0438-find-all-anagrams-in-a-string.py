class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_list= list(p)
        p_list.sort()

        for i in range(len(s)-len(p)+1):
            tmp = s[i:i+len(p)]
            tmp_list = list(tmp)
            tmp_list.sort()

            
            if tmp_list == p_list:
                result.append(i)
        return result
