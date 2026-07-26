class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        ret = []
        while i < len(nums):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < len(nums) and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while k >= 0 and nums[k] == nums[k + 1]:
                        k -= 1
                    continue
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
            while i < len(nums) and nums[i - 1] == nums[i]:
                i += 1
        return ret