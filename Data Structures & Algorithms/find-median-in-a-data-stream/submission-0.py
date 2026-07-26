class MedianFinder:

    def __init__(self):
        self.lowerHalf, self.upperHalf = [], []
        heapq.heapify(self.lowerHalf)
        heapq.heapify(self.upperHalf)

    def addNum(self, num: int) -> None:
        if self.lowerHalf and -self.lowerHalf[0] > num:
            heapq.heappush(self.lowerHalf, -num)
        else:
            heapq.heappush(self.upperHalf, num)
        
        lowerLength = (len(self.upperHalf) + len(self.lowerHalf)) // 2
        while len(self.lowerHalf) > lowerLength:
            heapq.heappush(self.upperHalf, -heapq.heappop(self.lowerHalf))
        while len(self.lowerHalf) < lowerLength:
            heapq.heappush(self.lowerHalf, -heapq.heappop(self.upperHalf))

    def findMedian(self) -> float:
        totalLength = len(self.lowerHalf) + len(self.upperHalf)
        if totalLength % 2:
            return self.upperHalf[0]
        return (-self.lowerHalf[0] + self.upperHalf[0]) / float(2)