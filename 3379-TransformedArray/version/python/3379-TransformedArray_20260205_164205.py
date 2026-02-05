# Last updated: 2/5/2026, 4:42:05 PM
1class Solution:
2    def constructTransformedArray(self, nums: List[int]) -> List[int]:
3        n=len(nums)
4        res=[-1]*n
5        for i in range(n):
6            if nums[i]>0:
7                inc=(i+nums[i])%n
8                res[i]=nums[inc]
9            elif nums[i]<0:
10                dec=(i-abs(nums[i]))%n
11                res[i]=nums[dec]
12            else:
13                res[i]=nums[i]
14        return res
15        
16                
17                
18                
19                
20        
21        