class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        maxProfit = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l += 1
            else:
                maxProfit = max(prices[r] - prices[l], maxProfit)
                r += 1
        return maxProfit