class LRUCache:

    def __init__(self, capacity: int):
        self.LRU={}
        self.capacity = capacity
    
    def getLRU(self):
        leastUsed = next(iter(self.LRU))
        del self.LRU[leastUsed]

    def get(self, key: int) -> int:
        if key in self.LRU:
            temp = self.LRU[key]
            del self.LRU[key]
            self.LRU[key]=temp
            return self.LRU[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            self.get(key)
        self.LRU[key]=value
        if len(self.LRU)>self.capacity:
            self.getLRU()
        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
print( obj.get(2))
print(obj.put(2,6))
print(obj.get(1))
print(obj.put(1,5))
print(obj.put(1,2))
print(obj.get(1))
print(obj.get(2))