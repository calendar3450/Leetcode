# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result1 =[]
        result2=[]

        def listNode1(node):
            if node ==None:
                return
            result1.append(node.val)
            listNode1(node.next)

        def listNode2(node):
            if node==None:
                return
            result2.append(node.val)
            listNode2(node.next)

        listNode1(l1)
        listNode2(l2)
        result1Reverse = ''
        result2Reverse = ''
        
        for i in range(len(result1)-1,-1,-1):
            result1Reverse +=str(result1[i])
        for i in range(len(result2)-1,-1,-1):
            result2Reverse +=str(result2[i])

        resultReverse = int(result1Reverse) +int(result2Reverse)
        resultReverseList= list(str(resultReverse))
        dummy =ListNode(0)
        current = dummy

        for i in range(len(resultReverseList)-1,-1,-1):
            current.next= ListNode(int(resultReverseList[i]))
            current = current.next

        return dummy.next

        