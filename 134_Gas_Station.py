class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        size = len(gas)
        diff = [gas[i]-cost[i] for i in range(size)]
        startPos=[]
        for i in range(size):
            if diff[i]>=0:
                startPos.append(i)
        
        for pos in startPos:
            i=0
            start=0
            flag=True
            while i<size:
                start+=diff[(pos+i)%size]
                if start < 0:
                    flag=False
                    break
                i+=1
            if flag:
                return pos
        return -1