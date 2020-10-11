class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points or len(points)<4:
            return 0
        xDict = {}
        for point in points:
            if point[0] in xDict:
                xDict[point[0]].add(point[1])
            else:
                xDict[point[0]]={point[1]}
        ans = 40000*40000 + 1
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1,y1=points[i][0],points[i][1] 
                x2,y2=points[j][0],points[j][1]
                if x1==x2 or y1==y2 or y2 not in xDict[x1] or y1 not in xDict[x2]:
                    continue
                area = abs(x1-x2)*abs(y1-y2)
                ans = min(ans,area)
        return ans if ans < 40000*40000 + 1 else 0