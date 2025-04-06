# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []
        for i in lists:
            current = i

            while current:
                result.append(current.val)
                current = current.next

        result.sort()
        dummy = ListNode(0)
        current = dummy
        for i in result:
            current.next = ListNode(i)
            current = current.next
        return dummy.next