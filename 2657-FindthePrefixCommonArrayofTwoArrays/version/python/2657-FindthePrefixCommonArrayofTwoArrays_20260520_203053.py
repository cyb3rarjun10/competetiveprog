# Last updated: 5/20/2026, 8:30:53 PM
1class Solution:
2    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
3        n = len(A)
4        ans = []
5        seen = [0] * (n + 1)
6        common = 0
7        
8        for i in range(n):
9            if seen[A[i]] == 0:
10                seen[A[i]] = 1
11            elif seen[A[i]] == 1:
12                common += 1
13            if seen[B[i]] == 0:
14                seen[B[i]] = 1
15            elif seen[B[i]] == 1:
16                common += 1
17            ans.append(common)
18        return ans