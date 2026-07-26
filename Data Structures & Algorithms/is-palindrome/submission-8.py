class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            while not self.alphaNum(s[p1]) and p1 < p2:
                p1 += 1
            while not self.alphaNum(s[p2]) and p1 < p2:
                p2 -= 1
            if s[p1].lower() != s[p2].lower():
                return False
            p1, p2 = p1 + 1, p2 - 1
        return True
    
    def alphaNum(self, c):
        if c.isdigit() or ord('z') >= ord(c.lower()) >= ord('a'):
            return True
        return False
        