class ZigzagIterator:
    def __init__(self, v1, v2):
        self.combined = []
        i,j=0,0
        while(i<len(v1) or j<len(v2)):
            if i<len(v1):
                self.combined.append(v1[i])
                i+=1
            if j<len(v2):
                self.combined.append(v2[j])
                j+=1

    def next(self) -> int:
        return self.combined.pop(0)

    def hasNext(self) -> bool:
        return len(self.combined)>0

# Your ZigzagIterator object will be instantiated and called as such:
i, v = ZigzagIterator([1,2],[3,4,5,6]), []
while i.hasNext(): v.append(i.next())
print(v)