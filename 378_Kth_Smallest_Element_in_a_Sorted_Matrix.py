from heapq import heapify, heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for x in matrix:
            for y in x:
                heap.append(y)
        heapify(heap)
        res = heap[0]
        for i in range(k):
            res = heappop(heap)
        return res