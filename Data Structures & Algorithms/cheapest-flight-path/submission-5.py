class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [float("inf")] * n
        distance[src] = 0
        for i in range(k + 1):
            copy = distance.copy()
            for source, dest, time in flights:
                if distance[source] != float("inf"):
                    copy[dest] = min(distance[source] + time, copy[dest])
            distance = copy
        return distance[dst] if distance[dst] != float("inf") else -1