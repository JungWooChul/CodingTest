# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        check = 0
        answer = ListNode()
        head = answer
        while l1 and l2:
            tmp = l1.val + l2.val + check
            head.next = ListNode(tmp%10)
            head = head.next
            check = tmp // 10
            
            l1, l2 = l1.next, l2.next
        
        if l1:
            while l1:
                tmp = l1.val + check
                head.next = ListNode(tmp%10)
                head = head.next
                check = tmp//10

                l1 = l1.next
        if l2:
            while l2:
                tmp = l2.val + check
                head.next = ListNode(tmp%10)
                head = head.next
                check = tmp//10

                l2 = l2.next
        if check:
            head.next = ListNode(check)
            head = head.next
        return answer.next
        