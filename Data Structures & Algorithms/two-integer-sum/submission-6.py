class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = dict()
        for i in range(len(nums)):
            if nums[i] in difference:
                return [difference[nums[i]], i]
            difference[target - nums[i]] = i
        return None