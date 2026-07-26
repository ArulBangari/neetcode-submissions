class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for ind, num in enumerate(nums):
            if target - num in diff:
                return [diff[target - num], ind]
            diff[num] = ind
        return None