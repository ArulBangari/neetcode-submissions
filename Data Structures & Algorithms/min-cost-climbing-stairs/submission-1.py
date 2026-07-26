class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        totalCost = [0] * (len(cost) + 2)
        for i in range(len(cost) - 1, -1, -1):
            totalCost[i] = cost[i] + min(totalCost[i + 1], totalCost[i + 2])
        return min(totalCost[0], totalCost[1])