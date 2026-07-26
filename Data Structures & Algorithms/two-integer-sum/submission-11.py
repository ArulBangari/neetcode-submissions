class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffDict = dict()
        for i in range(len(nums)):
            if target - nums[i] in diffDict:
                return [diffDict[target - nums[i]], i]
            diffDict[nums[i]] = i
        return None