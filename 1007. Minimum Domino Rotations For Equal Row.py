class Solution:
    def minDominoRotations(self, A, B) -> int:
        if len(A)==1:
            return 0
        mapA={}
        mapB={}
        mapAB={}
        for i in range(len(A)):
            mapA[A[i]]=mapA.get(A[i],0)+1
            mapB[B[i]]=mapB.get(B[i],0)+1
            
            mapAB[A[i]]=mapAB.get(A[i],0)+1
            if A[i]!=B[i]:
                mapAB[B[i]]=mapAB.get(B[i],0)+1
        
        minTurns = len(A)+1
        for val in mapAB:
            if mapAB[val]==len(A):
                if minTurns > min(mapA[val],mapB[val]):
                    minTurns = min(mapA[val],mapB[val])-(mapA[val]+mapB[val]-mapAB[val])
        return minTurns if minTurns < len(A) else -1

print(Solution().minDominoRotations([2,2],[1,3]))