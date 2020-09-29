from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        for num in nums:
            if num in frequency:
                frequency[num]+=1
            else:
                frequency[num]=1
        heap = [(-1*frequency[x],x) for x in frequency]
        heapify(heap)
        res=[]
        for i in range(k):
            res.append(heappop(heap)[1])
        
        return res