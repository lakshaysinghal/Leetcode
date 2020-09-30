class Solution:
    def numSquares(self, n: int) -> int:
        numOfSquares=[]
        numOfSquares.append(0)
        for i in range(1,n+1):
            squares=2**32
            j=1
            while(j*j<=i):
                squares = min(squares,numOfSquares[i-j*j]+1)
                j+=1
            numOfSquares.append(squares)
    
        return numOfSquares[n]