class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = defaultdict(int)
        for num in nums:
            numToFreq[num] += 1
        freqToNum =[[] for _ in range(len(nums))]
        for key, value in numToFreq.items():
            freqToNum[value - 1].append(key)
        ret = []
        i = len(freqToNum) - 1
        while len(ret) != k:
            if len(freqToNum[i]):
                for num in freqToNum[i]:
                    ret.append(num)
            i -= 1
        return ret