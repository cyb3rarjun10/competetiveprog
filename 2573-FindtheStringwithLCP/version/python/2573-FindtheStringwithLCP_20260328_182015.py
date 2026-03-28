# Last updated: 3/28/2026, 6:20:15 PM
1class Solution:
2    def findTheString(self, lcp: List[List[int]]) -> str:
3        n = len(lcp)
4        s_list = [""] * n
5        curr_char = 'a'
6        
7        for i in range(n):
8            if s_list[i] != "":
9                continue
10            if curr_char > 'z':
11                return ""
12            for j in range(i, n):
13                if lcp[i][j] > 0:
14                    s_list[j] = curr_char
15            curr_char = chr(ord(curr_char) + 1)
16        candidate_s = "".join(s_list)
17
18        def build_lcp(s):
19            n = len(s)
20            lcp_calc = [[0] * n for _ in range(n)]
21
22            for i in range(n - 1, -1, -1):
23                for j in range(n - 1, -1, -1):
24                    if s[i] == s[j]:
25                        if i == n - 1 or j == n - 1:
26                            lcp_calc[i][j] = 1
27                        else:
28                            lcp_calc[i][j] = 1 + lcp_calc[i + 1][j + 1]
29                    else:
30                        lcp_calc[i][j] = 0
31            return lcp_calc
32
33        if lcp == build_lcp(candidate_s):
34            return candidate_s
35            
36        return ""