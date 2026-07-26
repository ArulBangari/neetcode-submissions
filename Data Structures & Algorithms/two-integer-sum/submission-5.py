class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        while l < len(nums):
            r = 1
            while r < len(nums):
                if r == l:
                    r += 1
                    continue
                if nums[l] + nums[r] == target:
                    return [l, r]
                r += 1
            l += 1
        return None