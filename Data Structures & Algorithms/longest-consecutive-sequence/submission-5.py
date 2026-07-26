class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length_longest = 0

        for num in nums:
            if num - 1 not in nums_set:
                add = 1
                while num + add in nums_set:
                    add += 1
                length_longest = max(add, length_longest)
        return length_longest
                