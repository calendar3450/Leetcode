class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=collections.defaultdict(list)

        for i in strs:
            result[''.join(sorted(i))].append(i)
        return list(result.values())

                
            
        