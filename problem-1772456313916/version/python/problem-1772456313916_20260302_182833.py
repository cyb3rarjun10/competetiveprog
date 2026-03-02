# Last updated: 3/2/2026, 6:28:33 PM
1class Solution:
2    def minSwaps(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        rightmost = [-1] * n
5        
6        # HINT 1: Calculate the most right 1
7        idx = 0
8        for row in grid:
9            for i in range(n - 1, -1, -1):
10                if row[i] == 1:
11                    rightmost[idx] = i
12                    break
13            idx += 1
14            
15        # HINT 2: Check if answer exists
16        x = rightmost.copy()
17        x.sort()
18        for i in range(n):
19            if x[i] > i:
20                return -1
21                
22        # HINT 3: Simulate the swaps (Greedy, NOT Bubble Sort)
23        res = 0
24        for i in range(n):
25            # Find the FIRST row j (at or below i) that satisfies the condition <= i
26            target_idx = -1
27            for j in range(i, n):
28                if rightmost[j] <= i:
29                    target_idx = j
30                    break
31            
32            # Simulate swapping that specific row up to position i
33            while target_idx > i:
34                # Adjacent swap
35                rightmost[target_idx], rightmost[target_idx - 1] = rightmost[target_idx - 1], rightmost[target_idx]
36                target_idx -= 1
37                res += 1
38                
39        return res
40        
41
42        