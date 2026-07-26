class Solution:
    def rob(self, nums: List[int]) -> int:
        one = nums[-1]
        two = 0
        for i in range(len(nums) - 2, -1, -1):
            tmp = one
            one = max(one, nums[i] + two)
            two = tmp
        return one