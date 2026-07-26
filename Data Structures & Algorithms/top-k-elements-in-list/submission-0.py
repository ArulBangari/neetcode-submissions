class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        n = len(nums)
        # n arrays just in case all numbers are different in the array
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] += 1
        for key, value in count.items():
            freq[value - 1].append(key)
        n -= 1
        topk = []
        while len(topk) < k:
            for x in freq[n]:
                topk.append(x)
            n -= 1
        return topk