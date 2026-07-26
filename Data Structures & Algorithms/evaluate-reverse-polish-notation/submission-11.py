class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b + a)
            elif token == "-":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b - a)
            elif token == "*":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b * a)
            elif token == "/":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(int(b/a))
            else:
                stack.append(int(token))
        return stack[0]