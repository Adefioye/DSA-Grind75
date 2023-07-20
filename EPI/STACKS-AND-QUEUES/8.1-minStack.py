class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVals:
            self.minVals.append(val)
        else:
            self.minVals.append(min(self.minVals[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minVals.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVals[-1]
        