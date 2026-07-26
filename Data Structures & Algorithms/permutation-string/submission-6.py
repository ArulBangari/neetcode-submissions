class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1F = [0 for _ in range(26)]
        s2F = [0 for _ in range(26)]
        l = 0
        for char in s1:
            s1F[ord(char) - ord("a")] += 1
        
        for r in range(len(s2)):
            s2F[ord(s2[r]) - ord("a")] += 1

            while r - l >= len(s1):
                s2F[ord(s2[l]) - ord("a")] -= 1
                l += 1

            
            check = True
            for i in range(26):
                check = (s1F[i] == s2F[i]) and check

            if check:
                return True
        return False