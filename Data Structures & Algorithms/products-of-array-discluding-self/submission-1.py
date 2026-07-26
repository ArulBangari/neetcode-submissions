class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot_mul = 1
        check = False
        for num in nums:
            if num != 0 or check:
                tot_mul *= num
            else:
                check = True

        
        index = 0
        while index < len(nums):
            if check:
                if nums[index] == 0:
                    nums[index] = tot_mul
                else:
                    nums[index] = 0
            else:
                nums[index] = int(tot_mul / nums[index])
            index += 1
        return nums