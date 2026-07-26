class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in numSet:
                continue
            currNum = num
            while currNum in numSet:
                currNum += 1
            longest = max(currNum - num, longest)
        return longest