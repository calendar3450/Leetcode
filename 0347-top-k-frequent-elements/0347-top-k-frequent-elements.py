class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = list(set(nums))
        if k == len(a):
            return a
        d = []
        result= []
        for i in a:
            d.append([i,nums.count(i)])
        d.sort(key = lambda x: x[1], reverse= True)
        for i in range(k):
            result.append(d[i][0])
        return result
