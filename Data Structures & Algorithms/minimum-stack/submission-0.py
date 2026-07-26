class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = 2147483650

    def push(self, val: int) -> None:
        self.min_value = min(self.min_value, val)
        self.stack.append((val, self.min_value))

    def pop(self) -> None:
        if self.stack.pop()[0] == self.min_value:
            if self.stack:
                self.min_value = self.stack[-1][1]
            else:
                self.min_value = 2147483650

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()