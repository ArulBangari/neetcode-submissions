class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        x = [False] * (len(s) + 1)
        x[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s):
                    if (word == s[i:i + len(word)]) and x[i + len(word)]:
                        x[i] = True
                        break
        return x[0]