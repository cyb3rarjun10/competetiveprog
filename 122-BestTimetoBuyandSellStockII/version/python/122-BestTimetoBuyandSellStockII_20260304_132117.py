# Last updated: 3/4/2026, 1:21:17 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n=len(prices)
4        @cache
5        def recurse(idx,bought):
6            if idx==n:
7                return 0
8            if not bought:
9                buy=-prices[idx]+recurse(idx+1,True)
10                skip=recurse(idx+1,False)
11                return max(buy,skip)
12            else:
13                sell=prices[idx]+recurse(idx+1,False)
14                hold=recurse(idx+1,True)
15                return max(sell,hold)
16            
17        return recurse(0,False)