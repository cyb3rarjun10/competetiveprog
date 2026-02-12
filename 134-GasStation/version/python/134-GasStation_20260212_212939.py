# Last updated: 2/12/2026, 9:29:39 PM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        if sum(cost)>sum(gas):
4            return -1
5        res=0
6        tot=0
7        start=0
8        for i in range(len(cost)):
9            tot+=(gas[i]-cost[i])
10            if tot<0:
11                tot=0
12                start=i+1
13        return start
14                
15        
16
17