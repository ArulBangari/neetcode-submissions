class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        one = nums[-2]
        two = 0
        for i in range(len(nums) - 3, -1, -1):
            print(i, one, two)
            tmp = one
            one = max(one, nums[i] + two)
            two = tmp
        return max(one, two)