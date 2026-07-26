class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        letters = [0 for _ in range(26)]

        for char in s1:
            letters[ord(char) - 97] += 1
        
        L, R = 0, 0

        while R < len(s2):
            letters[ord(s2[R]) - 97] -= 1
            R += 1
            while letters[ord(s2[R - 1]) - 97] < 0:
                letters[ord(s2[L]) - 97] += 1
                L += 1
        
            if sum(letters) == 0:
                return True
        
        return False