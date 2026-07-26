class Solution:
    def minWindow(self, s: str, t: str) -> str:
        matches, l = 0, 0
        startIndex, endIndex = 0, len(s) + 1
        charFreq = defaultdict(int)
        for char in t:
            charFreq[char] += 1
        
        for r in range(len(s)):
            if s[r] in charFreq:
                charFreq[s[r]] -= 1
                if charFreq[s[r]] == 0:
                    matches += 1
            
            while matches == len(charFreq.keys()):
                if  endIndex - startIndex > r - l:
                    startIndex, endIndex = l, r + 1
                if s[l] in charFreq:
                    charFreq[s[l]] += 1
                    if charFreq[s[l]] > 0:
                        matches -= 1
                l += 1
        if endIndex - startIndex == len(s) + 1:
            return ""
        return s[startIndex: endIndex]