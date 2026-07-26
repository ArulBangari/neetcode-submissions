class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(' : ')', '{' : '}', '[': ']'}
        stack = []
        for char in s:
            if char in dict.keys():
                stack.append(char)
            else:
                if stack:
                    if char != dict[stack.pop()]:
                        return False
                else:
                    return False
        if stack:
            return False
        return True