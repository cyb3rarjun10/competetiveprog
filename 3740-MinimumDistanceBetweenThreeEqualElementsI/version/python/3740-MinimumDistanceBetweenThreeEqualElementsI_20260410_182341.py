# Last updated: 4/10/2026, 6:23:41 PM
1class Solution:
2    def minimumDistance(self, nums: List[int]) -> int:
3        def calmindist(arr):
4            mindist=float('inf')
5            for i in range(len(arr)-2):
6                mindist=min(mindist,abs(arr[i]-arr[i+1])+abs(arr[i+2]-arr[i+1])+abs(arr[i+2]-arr[i]))
7            return mindist
8                
9        d=Counter(nums)
10        dist=float('inf')
11        for val,count in d.items():
12            if count>=3:
13                ind=[i for i in range(len(nums)) if nums[i]==val]
14                dist=min(dist,calmindist(ind))
15        return dist if dist!=float('inf') else -1
16                
17                    
18                    
19            
20            
21        
22            
23                