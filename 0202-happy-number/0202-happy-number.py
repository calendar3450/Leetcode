class Solution:
    def isHappy(self, n: int) -> bool:
        def next(x):
            return sum(int(i)**2 for i in str(x))

        slow = n
        fast = next(n)

        while fast != 1 and fast != slow:
            slow = next(slow)
            fast = next(next(fast))

        return fast == 1