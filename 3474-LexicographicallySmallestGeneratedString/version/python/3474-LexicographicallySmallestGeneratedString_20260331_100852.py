# Last updated: 3/31/2026, 10:08:52 AM
1class Solution:
2    def generateString(self, str1: str, str2: str) -> str:
3        n, m = len(str1), len(str2)
4        s = ["a"] * (n + m - 1)
5        fixed = [False] * (n + m - 1)
6
7        # process the case of 'T'
8        for i, ch in enumerate(str1):
9            if ch == "T":
10                for j, c in enumerate(str2, i):
11                    if fixed[j] and s[j] != c:
12                        return ""
13                    s[j], fixed[j] = c, True
14
15        # process the case of 'F'
16        for i, ch in enumerate(str1):
17            if ch == "F":
18                # check if there are already different characters
19                if any(str2[j - i] != s[j] for j in range(i, i + m)):
20                    continue
21
22                # find the first modifiable position
23                for j in range(i + m - 1, i - 1, -1):
24                    if not fixed[j]:
25                        s[j] = "b"
26                        break
27                else:
28                    return ""
29
30        return "".join(s)