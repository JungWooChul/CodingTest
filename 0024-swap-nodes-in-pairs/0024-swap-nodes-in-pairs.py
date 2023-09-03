# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        swap = head
        while swap and swap.next:
            tmp = swap.next.val
            swap.next.val = swap.val
            swap.val = tmp
            
            swap = swap.next.next
        return head