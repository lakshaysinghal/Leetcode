class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        mapAB = {}
        mapCD = {}
        
        for i in range(len(A)):
            for j in range(len(B)):
                sumAB = A[i]+B[j]
                if sumAB in mapAB:
                    mapAB[sumAB]+=1
                else:
                    mapAB[sumAB]=1
                    
                sumCD = C[i]+D[j]
                if sumCD in mapCD:
                    mapCD[sumCD]+=1
                else:
                    mapCD[sumCD]=1
        
        result = 0
        for x in mapAB:
            if (-1*x) in mapCD:
                result+= mapAB[x]*mapCD[(-1*x)]
        
        return result
