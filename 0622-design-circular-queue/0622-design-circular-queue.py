class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None for _ in range(k)]
        self.start = 0
        self.end = 0
        self.k = k
        self.len = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.q[self.end] = value
            self.end = (self.end + 1) % self.k
            self.len += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.q[self.start] = None
            self.start = (self.start + 1) % self.k
            self.len -= 1
            
            # print(tmp, self.start, self.end)
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            print(self.q[self.start])
            return self.q[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            print(self.q[self.end - 1])
            return self.q[self.end - 1]

    def isEmpty(self) -> bool:
        if self.len == 0:
            return True 
        else:
            return False

    def isFull(self) -> bool:
        if self.len == self.k:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()