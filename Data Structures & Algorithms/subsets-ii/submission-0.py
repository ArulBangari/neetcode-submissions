class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            i += 1
            dfs(i, cur)
            cur.pop()
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            dfs(i, cur)
        dfs(0, [])
        return res