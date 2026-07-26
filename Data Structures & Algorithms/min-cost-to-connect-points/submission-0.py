class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = {i: [] for i in range(len(points))}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        
        visited = set()
        minHeap = [(0, 0)]
        cost = 0
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            cost += weight
            visited.add(node)
            for w2, nei in adjList[node]:
                heapq.heappush(minHeap, (w2, nei))
        return cost