class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.insert(0, (val, min(self.stack[0][1], val)))
        else:
            self.stack.insert(0, (val, val))

    def pop(self) -> None:
        self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0][0]

    def getMin(self) -> int:
        return self.stack[0][1]
