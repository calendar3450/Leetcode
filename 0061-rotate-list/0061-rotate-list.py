# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        queue = deque()
        node = head

        while node:
            queue.append(node.val)
            node = node.next

        queue.rotate(k)
        dummy = ListNode(0)
        cur = dummy

        for i in queue:
            cur.next = ListNode(i)
            cur = cur.next

        return dummy.next
        