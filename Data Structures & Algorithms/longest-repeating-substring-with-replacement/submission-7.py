class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength, l, r = 0, 0, 0
        charFrequency = defaultdict(int)
        maxChar = ""
        while r < len(s):
            charFrequency[s[r]] += 1
            if charFrequency[maxChar] < charFrequency[s[r]]:
                maxChar = s[r]
            
            numCharsChanged = r - l + 1 - charFrequency[maxChar]
            while numCharsChanged > k and l < r:
                charFrequency[s[l]] -= 1
                for char in charFrequency:
                    if charFrequency[char] > charFrequency[maxChar]:
                        maxChar = char
                print("Removing chars")
                print(l, r)
                l += 1
                numCharsChanged = r - l + 1 - charFrequency[maxChar]
            print("Right before max")
            print(l, r)
            maxLength = max(maxLength, r - l + 1)
            r += 1
        return maxLength