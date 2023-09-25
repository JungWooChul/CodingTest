# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import numpy as np

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answer_tmp = []
        answer = ListNode()
        head = answer
        for i in lists:
            tmp_head = i
            while tmp_head:
                answer_tmp.append(tmp_head.val)
                tmp_head = tmp_head.next
        
        for ans in sorted(answer_tmp):
            tmp = ListNode(ans)
            head.next = tmp
            head = head.next
        
        return answer.next
            
                
            
            