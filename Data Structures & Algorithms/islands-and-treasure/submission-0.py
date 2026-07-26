class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        def bfs(i, j):
            level = 0
            visit = set()
            q = collections.deque()
            q.append((i, j))
            while q:
                qLen = len(q)
                for l in range(qLen):
                    i, j = q.popleft()
                    visit.add((i, j))
                    if grid[i][j] == 0:
                        return level
                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for di, dj in directions:
                        x, y = i + di, j + dj
                        if (0 <= x < rows and 0 <= y < cols and
                        (x, y) not in visit and grid[x][y] != -1):
                            q.append((x,y))
                level += 1
            return 2147483647

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != -1:
                    grid[i][j] = bfs(i, j)