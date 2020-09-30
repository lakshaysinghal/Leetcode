class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numOfPaths=[[0 for x in range(n)] for y in range(m)]
        numOfPaths[m-1][n-1]=1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i<m-1:
                    numOfPaths[i][j]+=numOfPaths[i+1][j]
                if j<n-1:
                    numOfPaths[i][j]+=numOfPaths[i][j+1]
        return numOfPaths[0][0]

