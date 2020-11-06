from heapq import heapify,heappop
class Node:
    def __init__(self,pt):
        self.point = pt
        self.dist = (pt[0]**2) + (pt[1]**2)
    def __lt__(self,other):
        return self.dist < other.dist
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K < 1:
            return []
        customPoints = [Node(point) for point in points ]
        
        heapify(customPoints)
        result=[]
        for i in range(K):
            result.append(heappop(customPoints).point)
        return result