class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        bagOfNums = set()
        for num in nums:
            totCons = 1
            bagOfNums.add(num)
            currNum = num - 1
            while currNum in bagOfNums:
                totCons += 1
                currNum -= 1
            currNum = num + 1
            while currNum in bagOfNums:
                totCons += 1
                currNum += 1
            longest = max(totCons, longest)
        return longest