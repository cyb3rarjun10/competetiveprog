# Last updated: 1/31/2026, 12:00:03 PM
1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        for x in letters:
4            if x>target:
5                return x
6        return letters[0]