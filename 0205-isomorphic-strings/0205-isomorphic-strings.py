from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        defaultdict_s = defaultdict(int)
        defaultdict_t = defaultdict(int)
        result_s = ''
        compare = {}

        for i in s:
            defaultdict_s[i] +=1

        for i in t:
            defaultdict_t[i] +=1

        if len(defaultdict_s) != len(defaultdict_t):
            return False

        else:
            for i in range(len(s)):
                if s[i] not in compare:
                    compare[s[i]] = t[i]
                    result_s +=t[i]

                else:
                    result_s +=compare[s[i]]

        if result_s == t:
            return True
        else:
            return False

        