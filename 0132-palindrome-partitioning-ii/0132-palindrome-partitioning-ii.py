class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def dp(i):
            # The remaining string is already one palindrome
            if i == len(s):
                return -1

            ans = float('inf')

            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    # Take s[i:j+1] as one palindrome
                    # +1 for the cut after it
                    ans = min(ans, 1 + dp(j + 1))

            return ans

        return dp(0)