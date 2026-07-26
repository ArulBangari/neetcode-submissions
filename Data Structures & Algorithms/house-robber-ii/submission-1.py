class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.helper(nums[1:]), self.helper(nums[:len(nums) - 1]), nums[0])
    
    def helper(self, nums):
        if not nums:
            return 0
        one, two = nums[-1], 0
        for i in range(len(nums) - 2, -1, -1):
            one, two = max(one, two + nums[i]), one
        return one