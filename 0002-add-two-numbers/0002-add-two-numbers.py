# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_sum, l1_check = 0, 0
        while l1 != None:
            l1_sum += int(l1.val) * (10**l1_check)
            l1_check += 1
            l1 = l1.next
        
        l2_sum, l2_check = 0, 0
        while l2 != None:
            l2_sum += int(l2.val) * (10**l2_check)
            l2_check += 1
            l2 = l2.next
        
        answer_sum = l1_sum + l2_sum
        answer_head = ListNode(answer_sum%10)
        answer_tail = answer_head
        answer_sum = answer_sum//10
        while answer_sum > 0:
            newnode = ListNode(answer_sum%10)
            answer_tail.next = newnode
            answer_tail = answer_tail.next
            answer_sum = answer_sum//10
        
        return answer_head