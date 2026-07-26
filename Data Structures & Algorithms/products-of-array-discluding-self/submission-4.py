class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1 for _ in range(len(nums))]
        suffix_arr = [1 for _ in range(len(nums))]
        return_arr = []
        for i in range(1, len(nums)):
            prefix_arr[i] = prefix_arr[i - 1] * nums[i - 1]
            suffix_i = len(nums) - i
            suffix_arr[suffix_i - 1] = suffix_arr[suffix_i] * nums[suffix_i]
        for x,y in zip(prefix_arr, suffix_arr):
            return_arr.append(x*y)
        return return_arr