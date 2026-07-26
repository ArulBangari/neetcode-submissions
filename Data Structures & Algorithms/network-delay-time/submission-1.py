class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i: [] for i in range(n + 1)}
        for n1, n2, time in times:
            adjList[n1].append((n2, time))
        
        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            t = max(time, t)
            for node2, time2 in adjList[node]:
                heapq.heappush(minHeap, (time2 + time, node2))
        return t if len(visit) == n else -1