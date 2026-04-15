# Last updated: 4/15/2026, 4:47:46 PM
1class Solution:
2    def closestTarget(
3        self, words: List[str], target: str, startIndex: int
4    ) -> int:
5        ans = n = len(words)
6        for i, word in enumerate(words):
7            if word == target:
8                ans = min(ans, abs(i - startIndex), n - abs(i - startIndex))
9        return ans if ans < n else -1
10