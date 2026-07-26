class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        total = 1
        for i in range(1, len(nums)):
            ret[i] = ret[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            total *= nums[i + 1]
            ret[i] *= total

        return ret