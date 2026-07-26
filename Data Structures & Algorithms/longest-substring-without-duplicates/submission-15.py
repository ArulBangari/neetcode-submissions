class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bag = set()
        l, r = 0, 0
        maxSub = 0
        while r < len(s):
            while s[r] in bag:
                bag.remove(s[l])
                l += 1
            maxSub = max(maxSub, r - l + 1)
            bag.add(s[r])
            r += 1
        return maxSub