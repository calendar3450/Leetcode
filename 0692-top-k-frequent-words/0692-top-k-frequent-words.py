from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = []
        tmp = []
        dict_a = Counter(words)
        sorted_dict = sorted(dict_a.items(), key = lambda item: item[1], reverse = True)
        
        for i in range(len(dict_a)):
            tmp.append([sorted_dict[i][0],sorted_dict[i][1],words.index(sorted_dict[i][0])])

        tmp.sort(key= lambda x: (-x[1],x[0]))
        
        for i in range(k):
            ans.append(tmp[i][0])

        return ans