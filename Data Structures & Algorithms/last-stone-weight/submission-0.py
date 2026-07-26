class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while stones:
            if len(stones) == 1:
                return -1 * stones[0]
            
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x == y:
                continue
            heapq.heappush(stones, -max(y - x, x - y))
        return 0
