class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        totalIslands = 0
        visited = set()
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1" and (x, y) not in visited:
                    totalIslands += 1
                    q.append((x, y))
                    while q:
                        i, j = q.popleft()
                        if grid[i][j] == "1" and (i,j) not in visited:
                            visited.add((i,j))
                            if i + 1 < rows:
                                q.append((i + 1, j))
                            if i - 1 >= 0:
                                q.append((i - 1, j))
                            if j + 1 < cols:
                                q.append((i, j + 1))
                            if j - 1 >= 0:
                                q.append((i, j - 1))
        return totalIslands