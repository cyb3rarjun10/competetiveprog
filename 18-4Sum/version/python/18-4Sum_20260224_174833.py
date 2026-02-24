# Last updated: 2/24/2026, 5:48:33 PM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        nums.sort()
4        n = len(nums)
5        res = []
6        for i in range(n):
7            # Skip duplicate for the first number
8            if i > 0 and nums[i] == nums[i-1]:
9                continue
10                
11            for j in range(i + 1, n):
12                # Skip duplicate for the second number
13                if j > i + 1 and nums[j] == nums[j-1]:
14                    continue
15                
16                # Two-pointer logic starts here
17                left = j + 1
18                right = n - 1
19                
20                while left < right:
21                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
22                    
23                    if curr_sum == target:
24                        res.append([nums[i], nums[j], nums[left], nums[right]])
25                        
26                        # Skip duplicates for left and right pointers
27                        while left < right and nums[left] == nums[left + 1]:
28                            left += 1
29                        while left < right and nums[right] == nums[right - 1]:
30                            right -= 1
31                            
32                        left += 1
33                        right -= 1
34                    elif curr_sum < target:
35                        left += 1
36                    else:
37                        right -= 1
38                        
39        return res