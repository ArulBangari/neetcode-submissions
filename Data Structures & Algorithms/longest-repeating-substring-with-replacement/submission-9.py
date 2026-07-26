class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength, l, maxF = 0, 0, 0
        charFreq = defaultdict(int)

        for r in range(len(s)):
            charFreq[s[r]] += 1

            while r - l + 1 - max(charFreq.values()) > k:
                charFreq[s[l]] -= 1
                l += 1

            maxLength = max(r - l + 1, maxLength)
        return maxLength
            
