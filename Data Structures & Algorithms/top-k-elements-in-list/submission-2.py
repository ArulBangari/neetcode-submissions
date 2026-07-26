class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        frequency = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n,c in count.items():
            frequency[c].append(n)
        ret = []
        for x in range(len(frequency) - 1, 0, -1):
            if len(frequency[x]) > 0:
                ret.extend(frequency[x])
                if len(ret) == k:
                    return ret