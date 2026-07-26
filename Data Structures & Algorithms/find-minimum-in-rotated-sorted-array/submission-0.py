class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1)
    
    def binarySearch(self, nums, l, r):
        m = l + (r - l) // 2
        if m == l:
            return min(nums[l], nums[r])
        
        if nums[l] >= nums[r]:
            print(l, r)
            if nums[l] > nums[m]:
                return self.binarySearch(nums, l, m)
            else:
                return self.binarySearch(nums, m, r)
        else:
            return nums[l]