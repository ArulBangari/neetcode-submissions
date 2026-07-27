class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        bag = defaultdict(int)
        l, r = 0, 0
        maxLen = 0
        while r < len(s):
            currChar = s[r]
            bag[currChar] += 1
            if r - l + 1 - bag[currChar] <= k:
                maxFreq = max(maxFreq, bag[currChar])
            
            while r - l + 1 - maxFreq > k:
                leftChar = s[l]
                bag[leftChar] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen