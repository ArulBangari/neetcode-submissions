class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        print(self.tweetMap)
        print(self.followMap)
        minHeap = []
        res = []
        self.followMap[userId].add(userId)
        for followId in self.followMap[userId]:
            if self.tweetMap[followId]:
                index = len(self.tweetMap[followId]) - 1
                time, tweetId = self.tweetMap[followId][index]
                minHeap.append([time, tweetId, followId, index - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, tweetId, followId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetMap[followId][index]
                heapq.heappush(minHeap, [time, tweetId, followId, index - 1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
