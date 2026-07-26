class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_index = {} 
        for index, num in enumerate(nums):
            diff_index = difference_index.get(target - num, -1)
            if diff_index != -1:
                return [diff_index, index]
            difference_index[num] = index