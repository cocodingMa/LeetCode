class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        minPre, res = prices[0], 0
        for i in range(1, len(prices)):
            minPre = min(minPre, prices[i])
            res = max(res, prices[i]-minPre)
        return res