class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i1, longest = 0, 0
        charSet = set()
        for i2 in range(len(s)):
            while s[i2] in charSet:
                charSet.remove(s[i1])
                i1 += 1

            charSet.add(s[i2])
            longest = max(longest, i2 - i1 + 1)
        return longest
