# Last updated: 5/3/2026, 9:06:26 AM
1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3        n=len(s)
4        s=s+s
5        for i in range(n):
6            print(s[i:i+n])
7            if s[i:i+n]==goal:
8                return True
9        return False