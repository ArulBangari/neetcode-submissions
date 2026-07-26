class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i1, i2, longest = 0, 0, 0
        charSet = set()
        while i2 < len(s):
            while s[i2] in charSet:
                charSet.remove(s[i1])
                i1 += 1

            charSet.add(s[i2])
            i2 += 1
            longest = max(longest, i2 - i1)
        longest = max(longest, i2 - i1)
        return longest
