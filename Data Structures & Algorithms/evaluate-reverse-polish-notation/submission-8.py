class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        count = 0
        for token in tokens:
            print(stack)
            if len(stack) > 1:
                prev1 = int(stack[-1])
                prev2 = int(stack[-2])
            if token == "+":
                stack.pop()
                stack.pop()
                stack.append(prev2 + prev1)
            elif token == "-":
                stack.pop()
                stack.pop()
                stack.append(prev2 - prev1)
            elif token == "*":
                stack.pop()
                stack.pop()
                stack.append(prev2 * prev1)
            elif token == "/":
                stack.pop()
                stack.pop()
                res = prev2 // prev1
                if res < 0 and res != prev2 / prev1:
                    res += 1
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]