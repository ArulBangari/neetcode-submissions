class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapChars = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char not in mapChars:
                stack.insert(0, char)
            else:
                if stack and mapChars[char] == stack[0]:
                    stack.pop(0)
                else:
                    return False
        return len(stack) == 0