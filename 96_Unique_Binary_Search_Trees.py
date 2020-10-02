class Solution:
    def numTrees(self, n: int) -> int:
        dp =[1,1]
        for i in range(2,n+1):
            dp.append(0)
            for j in range(1,ceil(i/2)+1):
                dp[i]+= 2*dp[j-1]*dp[i-j] if i-j!=j-1 else dp[j-1]*dp[i-j]
                
                
        return dp[n]