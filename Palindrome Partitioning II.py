class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # is_pal[i][j] = True if s[i:j+1] is a palindrome
        is_pal = [[False] * n for _ in range(n)]
        
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
        
        # dp[i] = minimum cuts needed for s[:i+1]
        dp = [0] * n
        
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = float('inf')
                for j in range(i):
                    if is_pal[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[-1]
