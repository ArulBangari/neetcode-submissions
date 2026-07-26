class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_array = []
        nums_sorted = sorted(nums)
        for i in range(len(nums_sorted) - 2):
            if i == 0 or nums_sorted[i] != nums_sorted[i - 1]:
                j = i + 1
                k = len(nums) - 1
                target = -1 * nums_sorted[i]
                print(j)
                print(k)
                while j < k:
                    if nums_sorted[j] + nums_sorted[k] > target:
                        k -= 1
                    elif nums_sorted[j] + nums_sorted[k] < target:
                        j += 1
                    else:
                        add = [nums_sorted[i], nums_sorted[j], nums_sorted[k]]
                        if add not in return_array:
                            return_array.append(add)
                        j += 1
                        k -= 1
        return return_array