class Solution:
    def checkAlphanumeric(self, char):
        if ("a" > char or "z" < char) and ("0" > char or "1" < char):
            return False
        return True

    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        s_lower = s.lower()
        i1 = 0
        i2 = len(s) - 1

        while i1 < i2:
            if not self.checkAlphanumeric(s_lower[i1]):
                i1 += 1
                continue
            if not self.checkAlphanumeric(s_lower[i2]):
                i2 -= 1
                continue
            if s_lower[i1] != s_lower[i2]:
                return False
            
            i1 += 1
            i2 -= 1
        
        return True