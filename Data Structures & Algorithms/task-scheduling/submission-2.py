class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        maxHeap = [-freq for freq in freqs.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = collections.deque()
        while q or maxHeap:
            if q and q[0][1] == time:
                freq, idle = q.popleft()
                heapq.heappush(maxHeap, freq)
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                freq += 1
                if freq < 0:
                    q.append([freq, time + n + 1])
            time += 1
        return time