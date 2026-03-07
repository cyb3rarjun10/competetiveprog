# Last updated: 3/7/2026, 9:44:55 AM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        n=len(coins)
4        @cache
5        def dp(remcoins):
6            if remcoins==0:
7                return 0
8            if remcoins<0:
9                return float('inf')
10            mincoins=float('inf')
11            for c in coins:
12                curr=1+dp(remcoins-c)
13                mincoins=min(mincoins,curr)
14            return mincoins
15        x=dp(amount)
16        return x if x!=float('inf') else -1
17
18