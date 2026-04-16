# Last updated: 4/16/2026, 3:59:35 PM
1class Solution:
2    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
3        d = defaultdict(list)
4        n = len(nums)
5        
6        for i in range(n):
7            d[nums[i]].append(i)
8        
9        ans = []
10        
11        for q in queries:
12            target = nums[q]
13            l = d[target]
14            
15            if len(l) < 2:
16                ans.append(-1)
17                continue
18            
19            pos = bisect.bisect_left(l, q)
20            res = float('inf')
21            
22            # left neighbor
23            left = l[(pos - 1 + len(l)) % len(l)]
24            res = min(res, (q - left + n) % n, (left - q + n) % n)
25            
26            # right neighbor
27            right = l[(pos+1) % len(l)]
28            res = min(res, (q - right + n) % n, (right - q + n) % n)
29            
30            ans.append(res)
31        
32        return ans