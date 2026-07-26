class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        visit = set()
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        level = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = level
                for dr, dc in directions:
                    x, y = r + dr, c + dc
                    if (0 <= x < rows and 0 <= y < cols and
                        (x, y) not in visit and grid[x][y] == 2147483647):
                        q.append((x, y))
                        visit.add((x, y))
            level += 1