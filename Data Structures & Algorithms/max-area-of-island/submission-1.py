class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visit = set()
        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            area = 0
            while q:
                r, c = q.popleft()
                if (r, c) not in visit:
                    area += 1
                visit.add((r, c))
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    x, y = r + dr, c + dc
                    if (0 <= x < rows and 0 <= y < cols and
                        (x, y) not in visit and
                        grid[x][y]):
                        q.append((x, y))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r,c) not in visit:
                    maxArea = max(bfs(r, c), maxArea)
        return maxArea