class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphNum(c: str) -> bool:
            return (ord('0') <= ord(c) and ord('9') >= ord(c)) or (ord('a') <= ord(c) and ord('z') >= ord(c))
        sLower = s.lower()
        l, r = 0, len(sLower) - 1
        while l < r:
            while not isAlphNum(sLower[l]) and l < r:
                l += 1
            while not isAlphNum(sLower[r]) and l < r:
                r -= 1
            if sLower[l] != sLower[r]:
                return False
            l += 1
            r -= 1
        return True