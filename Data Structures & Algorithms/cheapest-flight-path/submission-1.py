class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k + 1):
            tmpPrices = prices.copy()
            for source, dest, price in flights:
                if prices[source] == float("inf"):
                    continue
                tmpPrices[dest] = min(tmpPrices[dest], price + prices[source])
            prices = tmpPrices
        return prices[dst] if prices[dst] != float("inf") else -1