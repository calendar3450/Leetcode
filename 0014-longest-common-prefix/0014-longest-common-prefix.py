class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        elif len(strs) == 1:
            return strs[0]

        common = ''
        for i in strs[0]:
            candidate = common + i
            if all(s.startswith(candidate) for s in strs):
                common = candidate
            else:
                break
        return common 

        