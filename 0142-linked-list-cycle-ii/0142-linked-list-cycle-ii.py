# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        
        # 1단계: 사이클 여부 확인
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # 2단계: 시작점 찾기
                pointer = head
                while pointer != slow:
                    pointer = pointer.next
                    slow = slow.next
                return pointer
        
        return None

        

        return None