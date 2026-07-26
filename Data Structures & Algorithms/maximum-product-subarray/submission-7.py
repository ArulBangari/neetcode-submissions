class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxProd, minProd = [0] * (n + 1), [0] * (n + 1)
        maxProd[-1], minProd[-1] = 1, 1
        for i in range(len(nums) - 1, -1, -1):
            maxProd[i] = max(nums[i] * maxProd[i + 1], nums[i] * minProd[i + 1], nums[i])
            minProd[i] = min(nums[i] * maxProd[i + 1], nums[i] * minProd[i + 1], nums[i])
        return max(maxProd[:-1])