# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []
        if not head:
            return head
        node = head
        while node:
            tmp.append(node.val)
            node = node.next

        tmp = tmp[::-1]
        
        dummy = ListNode(0)
        current = dummy
        for i in tmp:
            current.next = ListNode(i)
            current = current.next

        return dummy.next
        
        