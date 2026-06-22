class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))

        dist= strs[0]
        if len(strs) == 1:
            return dist

        comp = ""

        for i in dist:
            result = comp
            comp +=i
            total = 0

            for j in strs:
                if j.startswith(comp):
                    total += 1
            
            if total != len(strs):
                return result
                
        return comp