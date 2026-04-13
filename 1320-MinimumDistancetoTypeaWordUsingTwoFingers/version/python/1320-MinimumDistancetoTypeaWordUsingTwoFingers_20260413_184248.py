# Last updated: 4/13/2026, 6:42:48 PM
1class Solution:
2    def minimumDistance(self, word: str) -> int:
3        from functools import lru_cache
4
5        def dist(a, b):
6            if a == 26 or b == 26:
7                return 0
8            return abs(a//6 - b//6) + abs(a%6 - b%6)
9
10        @lru_cache(None)
11        def solve(i, f1, f2):
12            if i == len(word):
13                return 0
14
15            cur = ord(word[i]) - ord('A')
16
17            move1 = dist(f1, cur) + solve(i+1, cur, f2)
18            move2 = dist(f2, cur) + solve(i+1, f1, cur)
19
20            return min(move1, move2)
21
22        return solve(0, 26, 26)