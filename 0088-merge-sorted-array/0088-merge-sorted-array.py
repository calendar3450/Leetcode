class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp1 = nums1[:m]
        tmp2 = nums2[:n]
        tmp = tmp1+tmp2
        for i in range(len(tmp)):
            if i >=len(nums1):
                nums1.append(tmp[i])
            else:
                nums1[i]=tmp[i]

        nums1.sort()
        
