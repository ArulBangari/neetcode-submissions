class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        temp_max = -1001
        return_array = []
        for r in range(1, k):
            if nums[r] > nums[l]:
                l = r
            else:
                temp_max = max(temp_max, nums[r])
        
        return_array.append(nums[l])
        for r in range(k, len(nums)):
            temp_max = max(nums[r], temp_max)
            if nums[r] > nums[l]:
                l = r
                temp_max = -1001
            if r - l == k:
                while nums[l] != temp_max:
                    l += 1
                temp_max = nums[r]

            return_array.append(nums[l])
        return return_array