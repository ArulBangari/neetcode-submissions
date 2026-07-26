class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                temp = stack.pop() + stack.pop()
                stack.append(temp)
            elif char == "-":
                stack.append(-1 * stack.pop() + stack.pop())
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                temp = stack.pop()
                temp = int(stack.pop() / temp)
                stack.append(temp)
            else:
                stack.append(int(char))
        print(stack)
        return stack.pop()