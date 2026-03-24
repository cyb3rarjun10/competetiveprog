# Last updated: 3/24/2026, 7:18:23 PM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        total_sum = sum(nums)
4        if total_sum % 2 != 0:
5            return False
6            
7        n = len(nums)
8        target = total_sum // 2
9        
10        # Step 1: Create the 2D DP grid
11        dp = [[False] * (target + 1) for _ in range(n + 1)]
12        
13        # Step 2: Base Cases
14        for i in range(n + 1):
15            dp[i][0] = True
16            
17        # Step 3: Loop backwards through indexes
18        for idx in range(n - 1, -1, -1):
19            for rem in range(1, target + 1):
20                
21                # Step 4: The Rule (Replacing recurse() with dp[][])
22                take = False
23                if nums[idx] <= rem:
24                    take = dp[idx + 1][rem - nums[idx]]
25                
26                skip = dp[idx + 1][rem]
27                
28                dp[idx][rem] = take or skip
29                
30        # The final answer is starting at index 0, trying to reach 'target'
31        return dp[0][target]