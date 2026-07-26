class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = defaultdict(int)
        L, R, max_len = 0, 0, 0
        while R < len(s):
            letters[s[R]] +=  1
            check = True
            for letter in letters:
                if R - L - letters[letter] < k:
                    check = False
                    break
            if check:
                letters[s[L]] -= 1
                L += 1
            R += 1
            max_len = max(max_len, R - L)
        return max_len