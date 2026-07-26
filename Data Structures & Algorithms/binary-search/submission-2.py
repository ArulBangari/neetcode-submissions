class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            checkIndex = (l + r) // 2
            if nums[checkIndex] > target:
                r = checkIndex - 1
            elif nums[checkIndex] < target:
                l = checkIndex + 1
            else:
                return checkIndex
        return -1