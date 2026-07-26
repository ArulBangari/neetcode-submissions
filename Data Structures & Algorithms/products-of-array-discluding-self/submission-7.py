class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_array = [1 for _ in range(len(nums))]
        prefix = 1
        for i in range(0, len(nums)):
            return_array[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            return_array[i] *= postfix
            postfix *= nums[i]
        
        return return_array