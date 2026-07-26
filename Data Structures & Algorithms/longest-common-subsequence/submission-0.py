class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        dp = [[None] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows + 1):
            dp[i][cols] = 0
        for j in range(cols + 1):
            dp[rows][j] = 0
        
        def dfs(i, j):
            if dp[i][j] is not None:
                return dp[i][j]
            if text1[i] == text2[j]:
                total = 1 + dfs(i + 1, j + 1)
                dp[i][j] = total
                return total
            total = dp[i + 1][j] if dp[i + 1][j] is not None else dfs(i + 1, j)
            total = max(total, dp[i][j + 1] if dp[i][j + 1] is not None else dfs(i, j + 1))
            dp[i][j] = total
            return total
        return dfs(0, 0)