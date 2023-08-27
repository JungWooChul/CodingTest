# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        while head != None:
            tmp = ListNode(head.val)
            tmp.next = answer.next
            answer.next = tmp
            
            head = head.next
        return answer.next