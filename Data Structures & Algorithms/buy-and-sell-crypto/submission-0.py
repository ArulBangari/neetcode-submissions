class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 0
        difference = 0
        while R < len(prices):
            if prices[R] < prices[L]:
                L = R
            else:
                if prices[R] - prices[L] > difference:
                    difference = prices[R] - prices[L]
            R+= 1
        return difference