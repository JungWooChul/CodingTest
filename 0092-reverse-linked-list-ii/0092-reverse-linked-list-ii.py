# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        
        answer = []
        reverse_lst = []
        for i in range(len(lst)):
            if left-1 <= i < right-1:
                reverse_lst.append(lst[i])
            elif i == right-1:
                reverse_lst.append(lst[i])
                answer.extend(reverse_lst[::-1])
            else:
                answer.append(lst[i])
        
        answer_listnode = ListNode()
        node = answer_listnode
        for i in answer:
            node.next = ListNode(i)
            node = node.next
        return answer_listnode.next
                
            