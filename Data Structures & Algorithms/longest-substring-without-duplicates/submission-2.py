class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R, max_length = 0, 0, 0
        all_letters = set()
        for R in range(len(s)):
            if s[R] in all_letters:
                max_length = max(max_length, R - L)
                
                while s[L] != s[R]:
                    all_letters.remove(s[L])
                    L += 1

                L += 1
            else:
                all_letters.add(s[R])
                R += 1
        return max(max_length, R - L)