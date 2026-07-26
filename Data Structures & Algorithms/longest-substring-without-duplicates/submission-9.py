class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i1, i2, longest = 0, 0, 0
        charSet = set()
        while i2 < len(s) and i2 >= i1:
            if s[i2] in charSet:
                longest = max(longest, i2 - i1)
                while i2 > i1:
                    charSet.remove(s[i1])
                    if s[i2] == s[i1]:
                        i1 += 1
                        break
                    i1 += 1
            else:
                charSet.add(s[i2])
                i2 += 1
        longest = max(longest, i2 - i1)
        return longest
