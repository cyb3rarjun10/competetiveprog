# Last updated: 3/16/2026, 11:27:22 PM
1class Solution:
2    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
3        summ=sum(arr[:k])
4        res=0
5        if summ/k >= threshold:
6            res+=1
7        for i in range(k,len(arr)):
8            summ+=arr[i]
9            summ-=arr[i-k]
10            if summ/k >= threshold:
11                res+=1
12        return res