# Last updated: 3/23/2026, 4:52:23 PM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        coins.sort()
4        n=len(coins)
5        coinsneeded={}
6        coinsneeded[0]=0
7        for i in range(1,amount+1):
8            coinsneeded[i]=float('inf')
9        
10        for a in range(1,amount+1):
11            for coin in coins:
12                if coin>a:
13                    break
14                rem=a-coin
15                coinsneeded[a]=min(coinsneeded[a],1+coinsneeded[rem])
16        return coinsneeded[amount] if coinsneeded[amount]!=float('inf') else -1
17