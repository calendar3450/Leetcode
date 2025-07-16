class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        dic = {}
        for i in words:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] =1
        
        d1 = sorted(dic.items(), key=operator.itemgetter(1),reverse = True)

        for i,word in enumerate(d1):
            if i<k:
                result.append(d1[i][0])

        return result
