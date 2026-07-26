class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visit = set()

        def dfs(r, c):
            if ((r,c) in visit or r < 0 or r >= rows or 
                0 > c or c >= cols or grid[r][c] == 0):
                return 0

            visit.add((r, c))
            total = 1
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                x, y = r + dr, c + dc
                total += dfs(x, y)
            return total
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r,c) not in visit:
                    maxArea = max(dfs(r, c), maxArea)
        return maxArea