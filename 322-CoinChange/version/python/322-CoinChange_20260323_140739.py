# Last updated: 3/23/2026, 2:07:39 PM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        n=len(coins)
4        memo={}
5        for i in coins:
6            memo[i]=1
7        def dp(remcoins):
8            if remcoins in memo:
9                return memo[remcoins]
10            if remcoins==0:
11                return 0
12            if remcoins<0:
13                return float('inf')
14            mincoins=float('inf')
15            for c in coins:
16                curr=1+dp(remcoins-c)
17                mincoins=min(mincoins,curr)
18            memo[remcoins]=mincoins
19            return mincoins
20        x=dp(amount)
21        return x if x!=float('inf') else -1
22
23