class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_low = 1
        k_high = max(piles)
        while True:
            k_mid = (k_low + k_high) //2
            h_mid = 0
            if k_mid == k_low or k_mid == k_high:
                for banana in piles:
                    h_mid += math.ceil(banana / k_low)
                if h_mid <= h:
                    return k_low
                else:
                    return k_high

            for banana in piles:
                h_mid += math.ceil(banana / k_mid)
            
            if h_mid > h:
                k_low = k_mid
            
            else:
                k_high = k_mid