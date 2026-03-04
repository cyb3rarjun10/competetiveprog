# Last updated: 3/4/2026, 11:40:04 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        res=0
4        for i in range(len(prices)-1):
5            if prices[i]<prices[i+1]:
6                res+=abs(prices[i+1]-prices[i])
7        return res