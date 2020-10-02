class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        n,m = len(matrix),len(matrix[0])
        dp = [[0 for i in range(m)] for j in range(n)]
        result = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
                    result = max(result,dp[i][j])
        return result**2
