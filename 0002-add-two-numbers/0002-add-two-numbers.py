class Solution:
    # 이전 회차에서 진행했던 연결리스트의 역순을 취하는 함수
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 노드를 반복하며 값을 리스트에 추가하는 함수
    def toList(self, node: ListNode) -> ListNode:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬의 리스트를 역순 연결 리스트로 반환
    def toReversedLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        
        return node
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 연결리스트를 뒤집고 파이썬의 리스트 형태로 값 변환
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        # 덧셈 진행
        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        return self.toReversedLinkedList(str(resultStr))