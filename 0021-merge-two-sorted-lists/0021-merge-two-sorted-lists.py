# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result1 = []
        result2 = []
        
        if not list1:
            return list2
        elif not list2:
            return list1

        def listNode1(node):
            if node == None:
                return
            result1.append(node.val)
            listNode1(node.next)

        def listNode2(node):
            if node == None:
                return
            result2.append(node.val)
            listNode2(node.next)

        listNode1(list1)
        listNode2(list2)
        
        result = sorted(result1 + result2)
        dummy = ListNode(0)
        current = dummy
        for i in result:
            current.next = ListNode(i)
            current = current.next
        
        return dummy.next
        
        

        
                
            