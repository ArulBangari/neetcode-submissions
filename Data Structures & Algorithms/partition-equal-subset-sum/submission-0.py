class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target //= 2
        totalSet = set()
        totalSet.add(0)

        for num in nums:
            subSet = set()
            for n in totalSet:
                subSet.add(n)
                add = num + n
                if add == target:
                    return True
                subSet.add(add)
            totalSet = subSet
        return False