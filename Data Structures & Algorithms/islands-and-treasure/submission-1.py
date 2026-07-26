class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        level = 0
        while q:
            qLen = len(q)
            print(q, level)
            for i in range(qLen):
              i, j = q.popleft()
              grid[i][j] = min(level, grid[i][j])
              directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
              for di, dj in directions:
                x, y = i + di, j + dj
                if (0 <= x < rows and 0 <= y < cols and 
                    grid[x][y] == 2147483647):
                    q.append((x,y))
            level += 1