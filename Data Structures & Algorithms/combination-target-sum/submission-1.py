class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cands = []
        length = len(nums)
        def dfs(index, sumCand):
            if sumCand > target:
                return
            if sumCand == target:
                res.append(cands.copy())
                return
            for i in range(index, length):
                cands.append(nums[i])
                dfs(i, sumCand + nums[i]) 
                cands.pop()
        dfs(0, 0)
        return res