class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        for point in points:
            distance = -(math.sqrt(point[0]**2 + point[1]**2))
            heapq.heappush(minHeap, (distance, point))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [x[1] for x in minHeap]