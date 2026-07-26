class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        res = []
        nums.sort()
        length = len(nums) - 1
        print(len(nums) - 1)
        while i < len(nums) - 1:
            l = i + 1
            r = length
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return res
