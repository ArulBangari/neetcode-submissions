class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, buy):
            if i >= len(prices):
                return 0

            if (i, buy) in dp:
                return dp[(i, buy)]
            
            print(prices[i], buy, i)
            if buy:
                buying = dfs(i + 1, False) - prices[i]
                print(dp, buy)
                cooldown = dfs(i + 1, True)
            else:
                buying = dfs(i + 2, True) + prices[i]
                print(dp, buy)
                cooldown = dfs(i + 1, False)
            dp[(i, buy)] = max(buying, cooldown)
            return dp[(i, buy)]
        x = dfs(0, True)
        print(dp)
        return x