class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(nums, target, 0, len(nums) - 1)
    
    def binarysearch(self, nums, target, l, r) -> int:
        print(l, r)
        if l > r:
            return -1
        
        if nums[(l + r) // 2] > target:
            return self.binarysearch(nums, target, l, (l + r) // 2 - 1)
        elif nums[(l + r) // 2] < target:
            return self.binarysearch(nums, target, (l + r) // 2  + 1, r)
        else:

            return (l + r) // 2