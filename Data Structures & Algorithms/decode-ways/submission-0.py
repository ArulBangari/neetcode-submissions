class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [None for i in range(n)]
        dp[-1] = 1 if s[-1] != "0" else 0
        def dfs(i):
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            total = 0
            total += dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                total += dfs(i + 2)
            return total
        return dfs(0)