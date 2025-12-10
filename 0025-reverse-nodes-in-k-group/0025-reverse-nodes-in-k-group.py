# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = []

        def listNode(node):
            if not node:
                return

            result.append(node.val)
            listNode(node.next)
        
        listNode(head)
        n = len(result)

        for i in range(0, n, k):
            end = i + k
            if end > n:
                break
            result[i:end] = reversed(result[i:end])
        
        dummy = ListNode(0)
        current = dummy

        for j in result:
            current.next = ListNode(j)
            current = current.next

        return dummy.next
                