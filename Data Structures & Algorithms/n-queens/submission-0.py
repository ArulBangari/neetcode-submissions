class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = ['.' * n for _ in range(n)]
        res = []
        cols = [0 for _ in range(n)]
        diagL = [0 for _ in range(2 * n - 1)]
        diagR = [0 for _ in range(2 * n - 1)]
        def dfs(r):
            if r >= n:
                res.append(grid.copy())
            for c in range(n):
                if cols[c] > 0 or diagL[r + c] > 0 or diagR[r - c + n - 1] > 0:
                    continue
                s = grid[r] 
                grid[r] = s[:c] + 'Q' + s[c + 1:]
                cols[c] += 1
                diagL[r + c] += 1
                diagR[r - c + n - 1] += 1
                dfs(r + 1)
                grid[r] = s[:c] + '.' + s[c + 1:]
                cols[c] -= 1
                diagL[r + c] -= 1
                diagR[r - c + n - 1] -= 1
        dfs(0)
        return res