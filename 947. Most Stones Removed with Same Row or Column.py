'''
   12 22
01    21
00 10   
'''
class DSU:
    def __init__(self,capacity):
        self.parent = [x for x in range(capacity)]
        self.rank = [0 for x in range(capacity)]
    
    def find(self,item):
        if item !=self.parent[item]:
            self.parent[item]=self.find(self.parent[item])
        return self.parent[item]
    
    def union(self,item1,item2):
        parent1 = self.find(item1)
        parent2 = self.find(item2)
        
        if parent1==parent2:
            return
        
        if self.rank[parent1]>self.rank[parent2]:
            self.parent[parent2]=parent1
            self.rank[parent1]+=1
            self.rank[parent2]=0
        else:
            self.parent[parent1]=parent2
            self.rank[parent2]+=1
            self.rank[parent1]=0
    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        if not stones:
            return 0
        dsu = DSU(2*10000)
        for stone in stones:
            dsu.union(stone[0],stone[1]+10000)
        
        return len(stones) - len({dsu.find(stone[0]) for stone in stones})