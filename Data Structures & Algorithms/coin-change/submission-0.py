class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amtSet = set()
        q = collections.deque()
        q.append(amount)
        totalCoins = 0
        while q:
            for i in range(len(q)):
                amt = q.popleft()
                if amt == 0:
                    return totalCoins
                for coin in coins:
                    if amt - coin < 0 or amt - coin in amtSet:
                        continue
                    amtSet.add(amt - coin)
                    q.append(amt - coin)
            totalCoins +=1
        
        return -1