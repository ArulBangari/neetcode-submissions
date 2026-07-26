class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [0] * (n)
        for i in range(n - 1, - 1, -1):
            cache[i] = 1 + max([cache[j] for j in range(i + 1, n) if nums[j] > nums[i]] + [0])
        return max(cache)