class MyQueue:

    def __init__(self):
        self.enq = []
        self.deq = []

    def push(self, x):
        self.enq.append(x)

    def pop(self):
        self.enqToDeq()
        return self.deq.pop() 

    def peek(self):
        self.enqToDeq()
        return self.deq[-1] 

    def empty(self):
        return len(self.enq) == 0 and len(self.deq) == 0

    def enqToDeq(self):
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
