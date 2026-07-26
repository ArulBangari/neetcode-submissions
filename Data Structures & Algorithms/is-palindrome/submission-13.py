class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphNum(c: str) -> bool:
            return (ord('0') <= ord(c) and ord('9') >= ord(c)) or (ord('a') <= ord(c) and ord('z') >= ord(c))
        l, r = 0, len(s) - 1
        while l < r:
            while not isAlphNum(s[l].lower()) and l < r:
                l += 1
            while not isAlphNum(s[r].lower()) and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True