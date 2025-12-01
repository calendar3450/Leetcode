# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result1 = []
        result2 = []

        def linkedList1(node):
            if node == None:
                return
            result1.append(node.val)
            linkedList1(node.next)

        def linkedList2(node):
            if node == None:
                return
            result2.append(node.val)
            linkedList2(node.next)

        linkedList1(l1)
        linkedList2(l2)

        result1Str=''
        result2Str=''
        
        for i in range(len(result1)-1,-1,-1):
            result1Str += str(result1[i])

        for j in range(len(result2)-1,-1,-1):
            result2Str += str(result2[j])

        resultInt = int(result1Str) + int(result2Str)
        resultArr = []

        for k in str(resultInt):
            resultArr.append(k)

        dummy = ListNode(0)
        current = dummy 

        for l in range(len(resultArr)-1,-1,-1):
            current.next = ListNode(int(resultArr[l]))
            current = current.next

        return dummy.next