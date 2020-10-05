class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n= len(s)
        lps=[[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            lps[i][i]=1
        result = 1
        for palindromeLength in range(2,n+1):
            for i in range(n-palindromeLength+1):
                j = i+palindromeLength-1
                if i+1==j and s[i]==s[j]:
                    lps[i][j]=2
                elif s[i]==s[j]:
                    lps[i][j]=2+lps[i+1][j-1]
                elif s[i]!=s[j]:
                    lps[i][j]=max(lps[i+1][j],lps[i][j-1])
                if result < lps[i][j]:
                    result = lps[i][j]
        return result
