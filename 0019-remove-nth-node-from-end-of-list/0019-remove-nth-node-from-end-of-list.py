# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = []
        node = head
        while node:
            tmp.append(node.val)
            node= node.next
        
        tmp.pop(-n)
        
        dummy = ListNode(0)
        current = dummy
        for i in tmp:
            current.next = ListNode(i)
            current = current.next
        return dummy.next