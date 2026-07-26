class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffDict = dict()
        for i in range(len(nums)):
            if nums[i] in diffDict:
                return [diffDict[nums[i]], i]
            diffDict[target - nums[i]] = i
        return None