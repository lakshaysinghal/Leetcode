from heapq import heapify, heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [ -x for x in nums]
        heapify(heap)
        kthLargest = heap[-1]
        for i in range(k):
            kthLargest = heappop(heap)
        return -kthLargest