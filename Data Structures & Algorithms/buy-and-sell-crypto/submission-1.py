class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i1, i2 = 0, 0
        maxP = 0
        while i2 < len(prices):
            maxP = max(maxP, prices[i2] - prices[i1])
            if prices[i2] < prices[i1]:
                i1 = i2
            else:
                i2 += 1
        return maxP