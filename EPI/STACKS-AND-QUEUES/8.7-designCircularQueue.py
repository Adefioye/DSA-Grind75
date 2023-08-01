class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.head = self.tail = 0
        self.space = 0
        self.k = k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.space += 1
        self.queue[self.tail] = value 
        self.tail = (self.tail + 1) % self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False 
        self.space -= 1
        self.head = (self.head + 1) % self.k 
        return True


    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.head]
        

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.tail - 1]

    def isEmpty(self) -> bool:
        return self.space == 0

    def isFull(self) -> bool:
        return self.space == self.k
