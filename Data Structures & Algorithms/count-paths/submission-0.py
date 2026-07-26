class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0] * n for _ in range(m)]
        arr[m - 1][n - 1] = 1
        def dfs(i, j):
            if arr[i][j]:
                return arr[i][j]
            iM, jM = 0, 0
            if i + 1 < m:
                iM += arr[i + 1][j] if arr[i + 1][j] else dfs(i + 1, j)
            if j + 1 < n:
                jM += arr[i][j + 1] if arr[i][j + 1] else dfs(i, j + 1)
            arr[i][j] = iM + jM
            return arr[i][j]
        return dfs(0, 0)
