class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)
    
    def binarySearch(self, nums, target, l, r):
        m = l + (r - l) // 2
        if l == m:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            else:
                return -1

        if nums[l] > nums[r]:
            if nums[l] > nums[m]:
                if nums[m] > target:
                    return self.binarySearch(nums, target, l, m)
                else:
                    if nums[l] > target:
                        return self.binarySearch(nums, target, m, r)
                    elif nums[l] < target:
                        return self.binarySearch(nums, target, l, m)
                    else:
                        return l
            else:
                if nums[m] > target:
                    if nums[l] > target:
                        return self.binarySearch(nums, target, m, r)
                    elif nums[l] < target:
                        return self.binarySearch(nums, target, l, m)
                    else:
                        return l
                else:
                    return self.binarySearch(nums, target, m, r)
        else:
            if nums[m] > target:
                return self.binarySearch(nums, target, l, m)
            elif nums[m] < target:
                return self.binarySearch(nums, target, m, r)
            else:
                return m

