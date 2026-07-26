class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0] * n for _ in range(m)]
        arr[m - 1][n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                iM, jM = 0, 0
                if i == m - 1 and j == n - 1:
                    iM += 1
                if i + 1 < m:
                    iM += arr[i + 1][j]
                if j + 1 < n:
                    jM += arr[i][j + 1]
                arr[i][j] = iM + jM
        print(arr)
        return arr[0][0]