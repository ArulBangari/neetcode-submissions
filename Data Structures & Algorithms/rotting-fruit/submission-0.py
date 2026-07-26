class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        self.oneCount = 0
        time = 0
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.oneCount += 1
                
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
        
        def addFresh(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                x, y = r + dr, c + dc
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1 and (x,y) not in visit:
                    self.oneCount -= 1
                    visit.add((x, y))
                    q.append((x, y))

        time = 0
        while q:
            if self.oneCount == 0:
                return time
            for i in range(len(q)):
                r, c = q.popleft()
                addFresh(r, c)
            time += 1
        return time if self.oneCount == 0 else -1