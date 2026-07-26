class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = 1
        prefix = [0 for x in range(len(nums))]
        prefix_index = 0
        suffix_product = 1
        suffix = [0 for x in range(len(nums))]
        suffix_index = len(nums) - 1

        while prefix_index < len(nums):
            prefix[prefix_index] = prefix_product
            prefix_product *= nums[prefix_index]
            prefix_index += 1
        
        while suffix_index >= 0:
            suffix[suffix_index] = suffix_product
            suffix_product *= nums[suffix_index]
            suffix_index -= 1
        
        while suffix_index < len(nums):
            prefix[suffix_index] = prefix[suffix_index] * suffix[suffix_index]
            suffix_index += 1
        return prefix