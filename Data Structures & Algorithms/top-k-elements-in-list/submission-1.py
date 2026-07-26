class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        frequency = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num in count:
            frequency[count[num]].append(num)
        k_count = k
        ret = []
        ind = len(nums)
        while k_count > 0:
            if len(frequency[ind]) > 0:
                k_count -= len(frequency[ind])
                ret.extend(frequency[ind])
            ind -= 1
        return ret