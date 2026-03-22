# Last updated: 3/22/2026, 8:20:17 AM
1class Solution:
2    def uniformArray(self, nums1: list[int]) -> bool:
3        n=len(nums1)
4        c=0
5        for i in nums1:
6            if i%2==0:
7                c+=1
8        if n==c:
9            return True
10        nums1.sort(reverse=True)
11        if nums1[-1]%2==0:
12            return False
13        return True
14            
15        