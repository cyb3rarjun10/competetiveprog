# Last updated: 4/14/2026, 8:27:21 PM
1class Solution:
2    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
3        n = len(robot)
4        robot.sort()
5        factory.sort()
6        flat_factories = []
7        for pos, limit in factory:
8            for _ in range(limit):
9                flat_factories.append(pos)
10                
11        f = len(flat_factories)
12        @lru_cache
13        def dp(robo, facto):
14            if robo == n:
15                return 0
16            if facto == f:
17                return float('inf')
18
19            skip = dp(robo, facto + 1)
20            
21            dist = abs(robot[robo] - flat_factories[facto])
22
23            repair = dist + dp(robo + 1, facto + 1)
24            
25            return min(skip, repair)
26            
27        return dp(0, 0)
28            