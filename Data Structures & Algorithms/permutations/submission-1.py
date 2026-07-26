class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur, indices):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if i in indices:
                    continue
                cur.append(nums[i])
                indices.add(i)
                dfs(cur, indices)
                cur.pop()
                indices.remove(i)
        dfs([], set())
        return res