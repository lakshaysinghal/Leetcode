'''
ab cd
a b c d ab cd
a c b d ad
a c d b ab
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        merged=[intervals[0]]
        for i in range(1,len(intervals)):
            merged+=self.merge2(merged.pop(-1),intervals[i])
        return merged
    
    def merge2(self,it1,it2):
        if it1[0]>it2[0]:
            it1,it2=it2,it1
        if it1[0] <=it1[1] <it2[0]<=it2[1]:
            if it1[1]==it2[0]:
                return [it1[0],it2[1]]
            return [it1,it2]
        elif it1[0] <=it2[0] <=it1[1]<=it2[1]:
            return [[it1[0],it2[1]]]
        elif it1[0] <=it2[0] <=it2[1]<=it2[1]:
            return [[it1[0],it1[1]]]