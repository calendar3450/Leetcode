class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 초기값 설정
        res = nums[0]
        cur_max, cur_min = res, res

        for i in range(1, len(nums)):
            num = nums[i]
            
            # num이 음수일 때 max와 min이 뒤바뀌므로 swap
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
            
            # 현재 숫자와 (이전까지의 값 * 현재 숫자) 중 비교
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)
            
            # 전체 결과 업데이트
            res = max(res, cur_max)
            
        return res