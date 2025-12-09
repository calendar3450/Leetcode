# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        tmp = []

        node = head

        while node:
            tmp.append(node.val)
            node = node.next

        for i in range(0,len(tmp)-1,2):
            tmp[i],tmp[i+1] = tmp[i+1],tmp[i]
        
        dummy = ListNode(0)
        current = dummy
        for j in tmp:
            current.next = ListNode(j)
            current = current.next
       
        return dummy.next