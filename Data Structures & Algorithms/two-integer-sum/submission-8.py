class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_index = {} 
        for index, num in enumerate(nums):
            diff = target - num
            if diff in difference_index:
                return [difference_index[diff], index]
            difference_index[num] = index