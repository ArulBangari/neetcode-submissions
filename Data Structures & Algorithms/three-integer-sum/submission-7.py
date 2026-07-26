class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_array = []
        nums_sorted = sorted(nums)
        for i,a in enumerate(nums_sorted):
            if i == 0 or a != nums_sorted[i - 1]:
                j, k = i + 1, len(nums) - 1
                target = -1 * a
                while j < k:
                    if nums_sorted[j] + nums_sorted[k] > target:
                        k -= 1
                    elif nums_sorted[j] + nums_sorted[k] < target:
                        j += 1
                    else:
                        return_array.append([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                        j += 1
                        while nums_sorted[j] == nums_sorted[j- 1] and j < k:
                            j += 1
        return return_array