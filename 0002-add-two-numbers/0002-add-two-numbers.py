# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_l1=[]
        result_l2=[]
        result = []

        def listNode_l1(node):
            if node==None:
                return result_l1
            result_l1.append(node.val)
            listNode_l1(node.next)
        
        def listNode_l2(node):
            if node==None:
                return result_l2
            result_l2.append(node.val)
            listNode_l2(node.next)

        listNode_l1(l1)
        listNode_l2(l2)

        l1_str_reverse =''
        l2_str_reverse=''

        for i in range(len(result_l1)-1,-1,-1):
            l1_str_reverse+=str(result_l1[i])
        for i in range(len(result_l2)-1,-1,-1):
            l2_str_reverse+=str(result_l2[i])

        l1_int_reverse = int(l1_str_reverse)
        l2_int_reverse = int(l2_str_reverse)

        result_int = l1_int_reverse + l2_int_reverse

        for i in range(len(str(result_int))-1,-1,-1):
            result.append(str(result_int)[i])

        head = ListNode(int(result[0]))
        current_node = head

        for i in range(1,len(result)):
            current_node.next = ListNode(int(result[i]))
            current_node = current_node.next

        return head