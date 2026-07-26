class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        letters = defaultdict(int)
        l = 0
        lsmall, rsmall = 0, len(s) + 2

        for letter in t:
            letters[letter] += 1
    
        for r in range(len(s)):
            if s[r] in letters:
                letters[s[r]] -= 1
            
            check = True
            for letter in letters:
                if letters[letter] > 0:
                    check = False
            
            if check:
                while r > l:
                    if s[l] in letters:
                        if letters[s[l]] == 0:
                            break
                        else:
                            letters[s[l]] += 1
                    l += 1
                
                if r - l < rsmall - lsmall:
                    lsmall, rsmall = l, r
        return s[lsmall: rsmall + 1] if rsmall != len(s) + 2 else ""
                
            