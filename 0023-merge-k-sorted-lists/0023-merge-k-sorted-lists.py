# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        total = []
        
        def listNode(node):
            if not node:
                return 

            total.append(node.val)
            listNode(node.next)


        for i in lists:
            listNode(i)

        total.sort()

        dummy = ListNode(0)
        current = dummy

        for j in total:
            current.next = ListNode(j)
            current = current.next

        return dummy.next