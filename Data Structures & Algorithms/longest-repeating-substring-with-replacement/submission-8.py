class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength, l, r = 0, 0, 0
        charFrequency = defaultdict(int)
        maxF = 0
        while r < len(s):
            charFrequency[s[r]] += 1
            maxF = max(charFrequency[s[r]], maxF)
            
            while r - l + 1 - maxF > k:
                charFrequency[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r - l + 1)
            r += 1
        return maxLength