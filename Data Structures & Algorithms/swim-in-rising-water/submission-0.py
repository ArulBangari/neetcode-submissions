class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        totalTime = 0
        minHeap = [(grid[0][0], 0, 0)]
        rows, cols = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        while minHeap:
            time, x, y = heapq.heappop(minHeap)
            visited.add((x, y))
            totalTime = max(time, totalTime)
            if (x, y) == (rows - 1, cols - 1):
                return totalTime
            for dx, dy in dirs:
                i, j = x + dx, y + dy
                if (i, j) not in visited and 0 <= i < rows and 0 <= j < cols:
                    heapq.heappush(minHeap, (grid[i][j], i, j))