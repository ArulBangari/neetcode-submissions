class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []

        rows, cols = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(i, j):
            atlantic = False
            pacific = False
            q = collections.deque()
            q.append((i, j))
            visit = set()
            while q and (not atlantic or not pacific):
                i, j = q.popleft()
                if i == 0 or j == 0:
                    pacific = True
                if i == rows - 1 or j == cols - 1:
                    atlantic = True
                for di, dj in directions:
                    row, col = i + di, j + dj
                    if (0 <= row < rows and 0 <= col < cols and
                        heights[i][j] >= heights[row][col] and (row, col) not in visit):
                        q.append((row, col))
                        visit.add((row, col))
            return atlantic and pacific
        
        for r in range(rows):
            for c in range(cols):
                if bfs(r, c):
                    res.append((r, c))
        return res