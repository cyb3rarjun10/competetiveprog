# Last updated: 3/24/2026, 7:05:18 PM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        coins.sort(reverse=True)
4        @cache
5        def recurse(rem):
6            if rem==0:
7                return 0
8            minc=float('inf')
9            for c in coins:
10                if c<=rem:
11                    coi=1+recurse(rem-c)
12                    minc=min(minc,coi)
13            return minc
14        x=recurse(amount)
15        if x==float('inf'):
16            return -1
17        return x
18
19
20